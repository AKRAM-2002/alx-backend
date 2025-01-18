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


client.subscribe('ALXChannel');

client.on('message', (channel, message) => {
	console.log(message);

	if(message === 'KILL_SERVER') {
		client.unsubscribe(channel);
		client.quit();
	}
});
