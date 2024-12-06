# Queuing System in JS

## Description
This project implements a queuing system using Redis and Node.js. It covers fundamental concepts of queuing systems, Redis operations, and async operations in JavaScript.

## Learning Objectives
By the end of this project, you should be able to explain:
- How to run a Redis server on your machine
- How to perform basic operations with Redis client
- How to use Redis client with Node.js
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements
- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- Required files must be executable
- Code should use the `.js` extension
- Code will be tested using Jest and the command `npm run test`

## Required Files
- package.json
- .babelrc

## Tasks

### 0. Install a redis instance
- Download and compile Redis 5.0.7
- Start Redis server
- Test Redis server operation using ping
- Set and get values using Redis CLI
- Kill Redis server
- Copy dump.rdb to project root

### 1. Node Redis Client
- Create a Redis client
- Handle successful connection
- Handle connection errors
- File: `0-redis_client.js`

### 2. Node Redis client and basic operations
- Create functions for Redis operations:
  - setNewSchool: Set value for key
  - displaySchoolValue: Display value for key
- File: `1-redis_op.js`

### 3. Node Redis client and async operations
- Modify previous operations to use ES6 async/await
- Use promisify
- File: `2-redis_op_async.js`

### 4. Node Redis client and advanced operations
- Store hash values in Redis
- Use hset for multiple values
- Display hash using hgetall
- File: `4-redis_advanced_op.js`

### 5. Node Redis client publisher and subscriber
- Create publisher and subscriber
- Implement message handling
- Handle subscription channels
- Files: `5-subscriber.js`, `5-publisher.js`

### 6. Create the Job creator
- Create queue with Kue
- Create and manage jobs
- Handle job completion and failures
- File: `6-job_creator.js`

### 7. Create the Job processor
- Process jobs from queue
- Implement notification sending
- Handle job data
- File: `6-job_processor.js`

### 8. Track progress and errors with Kue: Create the Job creator
- Create multiple jobs
- Track job progress
- Handle job completion and failures
- File: `7-job_creator.js`

### 9. Track progress and errors with Kue: Create the Job processor
- Implement job processing
- Handle blacklisted phone numbers
- Track job progress
- File: `7-job_processor.js`

### 10. Writing the job creation function
- Create notification jobs
- Handle job creation validation
- File: `8-job.js`

### 11. Writing the test for job creation
- Implement test suite
- Test job creation
- Validate queue contents
- File: `8-job.test.js`

### 12. In stock?
- Create Express server
- Implement product management
- Handle stock reservation
- Integrate with Redis
- File: `9-stock.js`

## Installation
```bash
# Install dependencies
npm install

# Start Redis server
redis-server

# Run scripts
npm run dev <filename>
```

## Testing
```bash
npm test
```

## Author
- AKRAM BOUTZOUGA

## License
This project is part of the ALX SE curriculum.