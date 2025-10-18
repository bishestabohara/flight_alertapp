from us_airports import search_airports
import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import time
from config import Config

class FlightSearchAPI:
    def __init__(self):
        self.config = Config()
        self.access_token = None
        self.token_expires_at = None
    
    def get_access_token(self) -> str:
        """Get or refresh Amadeus API access token"""
        if self.access_token and self.token_expires_at and datetime.now() < self.token_expires_at:
            return self.access_token
        
        if not self.config.AMADEUS_API_KEY or not self.config.AMADEUS_API_SECRET:
            raise ValueError("Amadeus API credentials not configured")
        
        url = self.config.AMADEUS_TOKEN_URL
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.config.AMADEUS_API_KEY,
            'client_secret': self.config.AMADEUS_API_SECRET
        }
        
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()
            
            token_data = response.json()
            self.access_token = token_data['access_token']
            expires_in = token_data.get('expires_in', 3600)
            self.token_expires_at = datetime.now() + timedelta(seconds=expires_in - 60)
            
            return self.access_token
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to get access token: {e}")
    
    def search_flights(self, origin: str, destination: str, departure_date: str, 
                      return_date: str = None, adults: int = 1) -> List[Dict]:
        """Search for flights using Amadeus API"""
        token = self.get_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        
        url = f"{self.config.AMADEUS_BASE_URL}/shopping/flight-offers"
        
        params = {
            'originLocationCode': origin,
            'destinationLocationCode': destination,
            'departureDate': departure_date,
            'adults': adults,
            'max': 10  # Limit results
        }
        
        if return_date:
            params['returnDate'] = return_date
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            return self._parse_flight_data(data)
        except requests.exceptions.RequestException as e:
            print(f"Flight search error: {e}")
            return []
    
    def _parse_flight_data(self, data: Dict) -> List[Dict]:
        """Parse flight data from Amadeus API response"""
        flights = []
        
        if 'data' not in data:
            return flights
        
        for offer in data['data']:
            try:
                # Extract basic flight information
                price = float(offer['price']['total'])
                currency = offer['price']['currency']
                
                # Get flight details
                itineraries = offer.get('itineraries', [])
                if not itineraries:
                    continue
                
                outbound = itineraries[0]
                inbound = itineraries[1] if len(itineraries) > 1 else None
                
                flight_info = {
                    'price': price,
                    'currency': currency,
                    'outbound': self._parse_itinerary(outbound),
                    'inbound': self._parse_itinerary(inbound) if inbound else None,
                    'airlines': self._extract_airlines(offer),
                    'offer_id': offer.get('id', ''),
                    'last_ticketing_date': offer.get('lastTicketingDate', ''),
                    'number_of_bookable_seats': offer.get('numberOfBookableSeats', 0)
                }
                
                flights.append(flight_info)
            except (KeyError, ValueError, TypeError) as e:
                print(f"Error parsing flight data: {e}")
                continue
        
        return flights
    
    def _parse_itinerary(self, itinerary: Dict) -> Dict:
        """Parse individual itinerary (outbound or inbound)"""
        segments = []
        
        for segment in itinerary.get('segments', []):
            segment_info = {
                'departure': {
                    'airport': segment['departure']['iataCode'],
                    'terminal': segment['departure'].get('terminal', ''),
                    'time': segment['departure']['at']
                },
                'arrival': {
                    'airport': segment['arrival']['iataCode'],
                    'terminal': segment['arrival'].get('terminal', ''),
                    'time': segment['arrival']['at']
                },
                'airline': segment['carrierCode'],
                'flight_number': segment['number'],
                'aircraft': segment.get('aircraft', {}).get('code', ''),
                'duration': segment.get('duration', ''),
                'stops': len(segment.get('stops', []))
            }
            segments.append(segment_info)
        
        return {
            'duration': itinerary.get('duration', ''),
            'segments': segments
        }
    
    def _extract_airlines(self, offer: Dict) -> List[str]:
        """Extract unique airline codes from flight offer"""
        airlines = set()
        
        for itinerary in offer.get('itineraries', []):
            for segment in itinerary.get('segments', []):
                airlines.add(segment.get('carrierCode', ''))
        
        return list(airlines)
    
    def get_airport_suggestions(self, query: str) -> List[Dict]:
        """Get airport suggestions based on query"""
        token = self.get_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        
        url = f"{self.config.AMADEUS_BASE_URL}/reference-data/locations"
        params = {
            'subType': 'AIRPORT',
            'keyword': query,
            'max': 10
        }
        
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            airports = []
            
            for location in data.get('data', []):
                airports.append({
                    'code': location['iataCode'],
                    'name': location['name'],
                    'city': location.get('address', {}).get('cityName', ''),
                    'country': location.get('address', {}).get('countryName', '')
                })
            
            return airports
        except requests.exceptions.RequestException as e:
            print(f"Airport search error: {e}")
            return []

# Fallback flight search using mock data for demo purposes
class MockFlightSearch:
    def __init__(self):
        pass
    
    def search_flights(self, origin: str, destination: str, departure_date: str, 
                      return_date: str = None, adults: int = 1) -> List[Dict]:
        """Mock flight search for demo purposes"""
        import random
        
        # Generate mock flight data
        airlines = ['AA', 'DL', 'UA', 'WN', 'B6', 'NK', 'F9']
        base_price = random.randint(200, 800)
        
        flights = []
        for i in range(random.randint(3, 8)):
            price_variation = random.randint(-100, 200)
            price = max(150, base_price + price_variation)
            
            flight = {
                'price': price,
                'currency': 'USD',
                'airlines': [random.choice(airlines)],
                'offer_id': f'mock_{i}',
                'outbound': {
                    'duration': f"{random.randint(2, 8)}h {random.randint(0, 59)}m",
                    'segments': [{
                        'departure': {
                            'airport': origin,
                            'time': f"{random.randint(6, 22):02d}:{random.randint(0, 59):02d}"
                        },
                        'arrival': {
                            'airport': destination,
                            'time': f"{random.randint(8, 23):02d}:{random.randint(0, 59):02d}"
                        },
                        'airline': random.choice(airlines),
                        'flight_number': f"{random.choice(airlines)}{random.randint(100, 9999)}",
                        'stops': random.randint(0, 2)
                    }]
                },
                'inbound': None,
                'last_ticketing_date': departure_date,
                'number_of_bookable_seats': random.randint(1, 9)
            }
            
            if return_date:
                flight['inbound'] = {
                    'duration': f"{random.randint(2, 8)}h {random.randint(0, 59)}m",
                    'segments': [{
                        'departure': {
                            'airport': destination,
                            'time': f"{random.randint(6, 22):02d}:{random.randint(0, 59):02d}"
                        },
                        'arrival': {
                            'airport': origin,
                            'time': f"{random.randint(8, 23):02d}:{random.randint(0, 59):02d}"
                        },
                        'airline': random.choice(airlines),
                        'flight_number': f"{random.choice(airlines)}{random.randint(100, 9999)}",
                        'stops': random.randint(0, 2)
                    }]
                }
            
            flights.append(flight)
        
        return sorted(flights, key=lambda x: x['price'])
    
    def get_airport_suggestions(self, query: str) -> List[Dict]:
        """Get airport suggestions using comprehensive US airports database"""
        return search_airports(query)
