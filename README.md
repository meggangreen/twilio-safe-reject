# twilio-safe-reject
SafeReject lets registered users exchange fake contact information with persistent would-be suiters, aka Harassers.

The user sends an SMS to the Twilio number with their credentials, the
harasser's phone number (and name, if available), and the short place name
where the exchange took place (eg: 'the bar' or 'BART'). SafeReject updates
its database with the information and then texts the harasser from a 'fake
phone number' while impersonating the user. This allows the user time to
safely get away from the harasser before the genius act of treachery is
discovered.

NEW USERS can sign up online ONLY at this time. We need to be able to
verify real users, and also to have a list of people who can't use the
service because they have been flagged as a harasser. Online signup
uses two-step authentication to verify the device.

REGISTERED USERS can get a new fake phone number or initiate a number
exchange between a fake phone number and a harasser. We verify users
by the 'From' and their PIN.

HARASSERS have been previously texted by a fake phone number via a
registered user -- eg the user has tried to avoid exchanging contact
info, but the harasser just doesn't get it and was then passed into the
system by the registered user. The harasser is now trying to converse
with the registered user.

UNKNOWNS are probably would be harassers trying to get the numbers so
they can "catch" registered users. And also spambots. Jerks.

Twilio docs that I used:
https://www.twilio.com/docs/quickstart/python/sms
https://www.twilio.com/docs/tutorials/employee-directory-python-flask
