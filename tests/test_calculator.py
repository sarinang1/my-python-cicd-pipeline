"""
Unit tests for Calculator API
Tests all calculator operations and API endpoints
"""

import pytest
from app.calculator import Calculator, app


@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def calculator():
    """Create a Calculator instance for testing"""
    return Calculator()


# Test Calculator Class Methods
class TestCalculatorMethods:
    """Test the Calculator class methods directly"""
    
    def test_add(self, calculator):
        """Test addition"""
        assert calculator.add(5, 3) == 8
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
        assert calculator.add(1.5, 2.5) == 4.0
    
    def test_subtract(self, calculator):
        """Test subtraction"""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(3, 5) == -2
        assert calculator.subtract(0, 0) == 0
        assert calculator.subtract(10.5, 5.5) == 5.0
    
    def test_multiply(self, calculator):
        """Test multiplication"""
        assert calculator.multiply(5, 3) == 15
        assert calculator.multiply(-2, 3) == -6
        assert calculator.multiply(0, 100) == 0
        assert calculator.multiply(2.5, 4) == 10.0
    
    def test_divide(self, calculator):
        """Test division"""
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(9, 3) == 3
        assert calculator.divide(7, 2) == 3.5
        assert calculator.divide(-10, 2) == -5

    def test_power(self, calculator):
        """Test power operation"""
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 2) == 25
        assert calculator.power(10, 0) == 1
        assert calculator.power(3, 4) == 81

    
    def test_divide_by_zero(self, calculator):
        """Test division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)


# Test API Endpoints
class TestAPIEndpoints:
    """Test the Flask API endpoints"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get('/health')
        assert response.status_code == 200
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'calculator-api'
    
    def test_home(self, client):
        """Test home endpoint"""
        response = client.get('/')
        assert response.status_code == 200
        data = response.get_json()
        assert 'message' in data
        assert 'endpoints' in data
    
    def test_add_endpoint(self, client):
        """Test addition endpoint"""
        response = client.get('/add/5/3')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 8
        assert data['operation'] == 'addition'
        assert data['a'] == 5
        assert data['b'] == 3
    
    def test_subtract_endpoint(self, client):
        """Test subtraction endpoint"""
        response = client.get('/subtract/10/4')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 6
        assert data['operation'] == 'subtraction'
    
    def test_multiply_endpoint(self, client):
        """Test multiplication endpoint"""
        response = client.get('/multiply/7/6')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 42
        assert data['operation'] == 'multiplication'
    
    def test_divide_endpoint(self, client):
        """Test division endpoint"""
        response = client.get('/divide/20/4')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 5
        assert data['operation'] == 'division'
    
    def test_divide_by_zero_endpoint(self, client):
        """Test division by zero returns error"""
        response = client.get('/divide/10/0')
        assert response.status_code == 400
        data = response.get_json()
        assert 'error' in data
        assert 'Cannot divide by zero' in data['error']
    
    def test_floating_point_operations(self, client):
        """Test operations with floating point numbers"""
        response = client.get('/add/1.5/2.5')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 4.0
        
        response = client.get('/divide/7/2')
        assert response.status_code == 200
        data = response.get_json()
        assert data['result'] == 3.5


    def test_power_endpoint(self, client):
        """Test power endpoint"""
        response = client.get('/power/2/3')
        assert response.status_code == 200

        data = response.get_json()
        assert data['result'] == 8
        assert data['operation'] == 'power'
        assert data['base'] == 2
        assert data['exponent'] == 3



# Test Edge Cases
class TestEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_negative_numbers(self, client):
        """Test with negative numbers"""
        response = client.get('/add/-5/-3')
        assert response.status_code == 200
        assert response.get_json()['result'] == -8
        
        response = client.get('/multiply/-2/3')
        assert response.status_code == 200
        assert response.get_json()['result'] == -6
    
    def test_zero_operations(self, client):
        """Test operations with zero"""
        response = client.get('/add/0/0')
        assert response.status_code == 200
        assert response.get_json()['result'] == 0
        
        response = client.get('/multiply/100/0')
        assert response.status_code == 200
        assert response.get_json()['result'] == 0
    
    def test_large_numbers(self, client):
        """Test with large numbers"""
        response = client.get('/add/999999/1')
        assert response.status_code == 200
        assert response.get_json()['result'] == 1000000
