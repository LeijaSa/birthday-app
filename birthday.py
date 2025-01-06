
from datetime import datetime
import re


class BirthdayApplication:
    def __init__(self):
        self.__names=[]
        self.__birthdays=[]


    def get_sorted_birthdays(self):
        all=dict(zip(self.__names,self.__birthdays))
        latest_birthday = max(all.values())
        earliest_birthday = min(all.values())

        oldest_people = [name for name, birthday in all.items() if birthday == earliest_birthday]
        youngest_people = [name for name, birthday in all.items() if birthday == latest_birthday]

        print("Oldest person/people:")
        for person in oldest_people:
            print(f"- {person}")

        print("Youngest person/people:")
        for person in youngest_people:
            print(f"- {person}")
     
   
    def validate_dates(self):
        day_pattern=r"^([1-9]|0[1-9]|[12][0-9]|3[01])([./-])([1-9]|0[1-9]|1[1-2])\2[0-9]{4}$"
        for i in range(len(self.__birthdays)):
            date = self.__birthdays[i]
            validated_date=re.match(day_pattern, date)
            if not validated_date:
                print(f"One of dates ({date}) is not proper date")
                return False
            
            date_separator=date[-5]
            d,m,y=date.split(date_separator)
            date_birthday=datetime(int(y),int(m),int(d))
            if date_birthday>datetime.now() or int(y) < 1900:
                print(f"Birthday ({date}) cannot be in the future or before the year 1900")
                return False
            self.__birthdays[i] = date_birthday
                     
        return True

    def handle_entries(self,entries):

        name_pattern=r"^(?!.*[./-])[A-Za-z]+\Z"
        
        self.__names=[entry for entry in entries if re.match(name_pattern, entry)]
        self.__birthdays=[entry for entry in entries if not re.match(name_pattern, entry)]
            
        return self.validate_dates()

    def execute(self):

        while True:
            print("Names should consist only of letters, while birthdays must follow one of these formats: (0)3.(0)2.2001, 3/12/2001, or 3-12-2001")
            user_entry = input("Add name(s) and birthday(s): ")
            entries = user_entry.split()

            if len(entries)<2:      
                print("Please ensure names and birthdays are separated by a space.")
            elif len(entries)%2 !=0:
                print("Each entry must contain a corresponding name and birthday.")
            else:
                checked_entries=self.handle_entries(entries)
                if checked_entries:
                    self.get_sorted_birthdays()
                    break
        

application = BirthdayApplication()
application.execute()