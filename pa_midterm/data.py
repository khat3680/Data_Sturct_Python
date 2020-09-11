class Student:
    def __init__(self,sid,last,first):
        """
        -------------------------------------------------------
        Description:
            Initializes a Student Object
            Stores student id, last name and first name
            Higher 4 digits in student id represent enrolment year
        Use: student = Student(sid, last, first)
        -------------------------------------------------------
        Parameters:
            sid - seven digit student id (int)
            last - student last name (str)
            first - student first name (str) 
        Returns:
            A Student object (Student)            
        -------------------------------------------------------
        """
        self.sid = sid
        self.last = last
        self.first = first
    
    def __str__(self):
        """
        -------------------------------------------------------
        Description:
            Converst a Student Object to a string
        Use: my_string = str(student_object)
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            'sid:last,first'           
        -------------------------------------------------------
        """
        return str(self.sid) + ':'+self.last + ',' + self.first
    
    def list(self):
        """
        -------------------------------------------------------
        Description:
            Converst a Student object to a list
        Use: my_list = student_object.list()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            [sid,last,first]           
        -------------------------------------------------------
        """
        return [self.sid,self.last,self.first]
    
    def key(self):
        """
        -------------------------------------------------------
        Description:
            Define a student key, which is the same as sid
        Use: student_key = student_object.key()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            sid - student id (int)           
        -------------------------------------------------------
        """
        return self.sid
    
    def get_year(self):
        """
        -------------------------------------------------------
        Description:
            Returns the enrolment year of the student
        Use: y = student_obj.get_year()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            year - student enrolment year (int)           
        -------------------------------------------------------
        """
        return int(str(self.sid)[:4])
    
    def get_name(self):
        """
        -------------------------------------------------------
        Description:
            Returns the full name of a student in the following format
            'first last'
        Use: name = student_obj.get_name()
        -------------------------------------------------------
        Parameters:
            None
        Returns:
            name - student full name (str)           
        -------------------------------------------------------
        """
        return self.first + ' ' + self.last
    
    def __gt__(self,other):
        if self.key() > other.key():
            return True
        elif self.key() < other.key():
            return False
        elif self.last > other.last:
            return True
        elif self.last < other.last:
            return False
        elif self.first > other.first:
            return True
        return False
    
    def __lt__(self,other):
        if self.key() < other.key():
            return True
        elif self.key() > other.key():
            return False
        elif self.last < other.last:
            return True
        elif self.last > other.last:
            return False
        elif self.first < other.first:
            return True
        return False

    def __eq__(self,other):
        return self.key() == other.key() and self.last == other.last and self.first == other.first
    
    def __ge__(self,other):
        return self > other or self == other
    
    def __le__(self,other):
        return self < other or self == other
    
    def __ne__(self,other):
        return not self == other

class Process:
    def __init__(self,PID,time,arrival):
        assert isinstance(PID,int) and len(str(PID)) == 10, 'Invalid PID'
        assert isinstance(time,int) and time>=0, 'Invalid time'
        assert isinstance(arrival,int) and arrival >=0, 'Invalid arrival'
        self.PID = PID
        self.time = time
        self.arrival = arrival
    
    def __str__(self):
        output = '['+str(self.arrival)+']('+str(self.PID)+','+str(self.time)+')'
        return output
    
    def key(self):
        return self.PID
    
    #time then arrival then PID
    def __eq__(self,other):
        return self.arrival == other.arrival and self.time == other.time and self.PID == other.PID
    
    def __ne__(self,other):
        return not self == other
    
    def __gt__(self,other):
        if self.arrival > other.arrival:
            return True
        if self.arrival < other.arrival:
            return False
        #equal arrival
        if self.time > other.time:
            return True
        if self.time < other.time:
            return False
        #equal arrival and time
        if self.PID > other.PID:
            return True
        return False
    
    def __ge__(self,other):
        return self == other or self > other
    
    def __lt__(self,other):
        if self.arrival < other.arrival:
            return True
        if self.arrival > other.arrival:
            return False
        #equal arrival
        if self.time < other.time:
            return True
        if self.time > other.time:
            return False
        #equal arrival and time
        if self.PID < other.PID:
            return True
        return False
    
    def __le__(self,other):
        return self == other or self < other
