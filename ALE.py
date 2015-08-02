"""
Asynchronous Learning Engine (ALE)

Supports PWS standard desktop (studio)
Mentor Queues
Load Balancing / Air Traffic Control
Courses / Flights

A mentor queue is a worker queue with
tasks pending, in process, complete.
The many subclasses of Task are only hinted
at in this overview.

Example Tasks (Transactions archiving to Chronofile):
Set start time on booked flight, notify students
Take Off
In-flight Services (the learning experience)
Land
Postmortem **/ Archive Stats

** sounds dire and we do try experimental courses
sometimes that "crash" but in this shoptalk it's
how we discuss any completed flight.

In-flight the students have a Call Bell for
special services.  We run "shows" which in the
better schools are highly interactive and require
a lot of student activity.  Passivism is a killer
when it comes to building confidence and competence
in one's tools, as Scott Gray would point out during
faculty meetings.

A normal / standard flight consists of working
through course materials in a PWS Studio with
asynchronous feedback from one or more mentors.
The "flight" (course) is also a unit of accounting
i.e. we containerize it in terms of fixed cost
overhead, tuition, compensation and so on.  See
workflow diagrams.

ALE:

In the OO version, ALE is the root object, adding mixins as needed

Kirby Urner

Want graphics?
https://www.flickr.com/photos/kirbyurner/sets/72157654417641521

"""

class Flight(ALE):
    pass
    
class AirTrafficUtils(ALE):
    pass

class Passenger(AWS):
    pass

class PWS:
    pass

class Dispatcher(AirTrafficUtils):
    pass

class Student(Passenger):
    pass

class Task:
    # Examples:  Start Class, Submit Work, Annotate Materials, Return Work
    pass

class Mentor(Oasis):  # # Example mixin (ways to "phone home")
    pass

class Course(Flight): # Expense Unit for accounting / bookkeeping
    pass
    
class Oversight(ALE):
    pass

class Admin(Oversight):
    pass

class Recruiting(Mentor):
    pass  # Exhibited Mentors, free samples

class StudentSupport(Oversight):
    pass  # guidance functions ("Travel Agency")


