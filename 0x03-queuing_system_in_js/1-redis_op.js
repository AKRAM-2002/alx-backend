import redis from "redis";

// Create Redis client
const client = redis.createClient();

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});

// Function to set a value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print); // Use redis.print for confirmation
}

// Function to get a value from Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error('Error retrieving value:', err);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions
displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
setNewSchool('ALX', '1')
displaySchoolValue('ALX')