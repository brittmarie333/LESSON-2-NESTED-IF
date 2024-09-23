#Task 2: Venue Selection
#Based on the corrected code from Task 1, 
# further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room" 
print(venue)

if venue is "large hall":
    print("Your event will be in the large hall with an audio system!")
elif venue is "conference room":
    print("Your event will be in the conference room with a projecter!")