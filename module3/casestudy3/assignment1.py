
import Customer

# Not eligible Case
classObject = Customer('iPhone-14', '12222', 1)
print(classObject.createOrder())


# elgible case
csOrder = Customer('Macbook', '12222erer', 0)
print(csOrder.createOrder())



























# #  class to store the user data
# class CustomerData:
#     def __init__(self,title, first_name, last_name, blacklisted = 0 ):
#         self.title = title
#         self.first_name = first_name
#         self.last_name = last_name
#         self.blacklisted = blacklisted
    
#     def getTitle(self):
#         return self.title
#     def getFirstName(self):
#         return self.first_name
#     def getLastName(self):
#         return self.last_name
#     def getIsBlackListed(self):
#         return self.blacklisted
#     def getCustomer(self):
#         return {'title':self.title, 'first_name':self.first_name, 'last_name':self.last_name, "blacklisted":self.blacklisted}

# # reading files
# readingfile = open('FairDealCustomerData.csv', 'r')
# csvFile = csv.reader(readingfile)

# classObjects = [] 
# # loop over list and storing data in class

# # Full name customers
# fullname_data = list([data for data in csvFile if re.match(
#     r"([a-zA-Z].+)\s(\w+)\s(\w+)", data[1].strip(), re.IGNORECASE)])

# for lines in fullname_data:
#     name_split = lines[1].split('.')
#     # creating unique class object for users , title, first_name, last_name, blacklist status
#     CustomerData(name_split[0], lines[0],name_split[1], lines[2])

