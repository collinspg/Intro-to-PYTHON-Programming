print('please enter the following information')
#Request for Main Information
firstName = input('First name:')
lastName = input('Last name:')
eMail = input('Email:')
phone = input('Phone number:')
jobTitle = input('Job title:')
idNum = input('ID Number:')
#Request for additional information
hairColour = input('Hair: ')   
eyeColour = input('Eye: ')        
startMonth = input('Month: ')    
training =  input('Training: ')      
#End of information request/Begin print for Main Information
print()
print('The ID card is:' )
print('--------------------------------------------------------------------------------')
print(f"{lastName.upper()},{firstName.capitalize()}")
print(jobTitle.title())
print(f"ID: {idNum}")
print()
print(eMail.lower())
print(phone)
print()
#end of print for Main Information/Begin print for Additional Information.
print(f"Hair: {hairColour},              Eye:{eyeColour}")               
print(f"Month:{startMonth},          Training: {training}")          

