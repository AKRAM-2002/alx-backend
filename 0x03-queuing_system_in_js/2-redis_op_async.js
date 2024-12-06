import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

// Promisify the Redis GET method
const getAsync = promisify(client.get).bind(client);

// Function to set a new school
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

// Function to display school value using async/await
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.error(`Error fetching value for ${schoolName}:`, err);
    }
}

// Test the functions
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
