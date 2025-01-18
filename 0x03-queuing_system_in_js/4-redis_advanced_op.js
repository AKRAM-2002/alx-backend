import redis from 'redis';

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

// Function to set a hash in Redis
function setNewHash() {
    const key = 'ALX';
    const cities = {
        Portland: 50,
        Seattle: 80,
        'New York': 20,
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };

    Object.entries(cities).forEach(([city, value]) => {
        client.hset(key, city, value, redis.print);
    });
}

// Function to display the hash from Redis
function displayHash() {
    const key = 'ALX';
    client.hgetall(key, (err, result) => {
        if (err) {
            console.error('Error fetching hash:', err);
            return;
        }
        console.log(result);
    });
}

// Set the hash and then display it
setNewHash();
displayHash();
