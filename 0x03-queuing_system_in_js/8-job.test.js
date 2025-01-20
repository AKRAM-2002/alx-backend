import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
import sinon from 'sinon';


describe('createPushNotificationsJobs', () => {
	let queue;

	beforeEach(() => {
		queue = kue.createQueue();
		queue.testMode.enter();
	});

	afterEach(() => {
	// Clear queue and exit test mode
		queue.testMode.clear();
		queue.testMode.exit();
	});

	it('should display an error if jobs is not an array', () => {
		expect(() => createPushNotificationsJobs('not an array', queue)).to.throw(
			Error,
			'Jobs is not an array'
		);
	});

	it('should create new jobs in the queue', () => {
		    const jobs = [
			          { phoneNumber: '1234567890', message: 'Message 1' },
			          { phoneNumber: '9876543210', message: 'Message 2' },
			        ];

		    createPushNotificationsJobs(jobs, queue);

		    expect(queue.testMode.jobs.length).to.equal(2);
		    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
		    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
		    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
		  });

	  it('should log the job creation process', () => {
		      const jobs = [
			            { phoneNumber: '1234567890', message: 'Message 1' },
			          ];

		      console.log = sinon.spy();
		      createPushNotificationsJobs(jobs, queue);

		      expect(console.log.calledWith('Notification job created: 1')).to.be.true;
		    });
});

