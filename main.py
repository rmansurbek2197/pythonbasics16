class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

class Slot:
    def __init__(self, slot_id, slot_type):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.is_available = True
        self.vehicle = None

    def park(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
            return f"Vehicle {vehicle.license_plate} parked in slot {self.slot_id}"
        else:
            return "Slot is not available"

    def leave(self):
        if not self.is_available:
            self.is_available = True
            vehicle = self.vehicle
            self.vehicle = None
            return f"Vehicle {vehicle.license_plate} left slot {self.slot_id}"
        else:
            return "Slot is already empty"

class Ticket:
    def __init__(self, vehicle, slot, entry_time):
        self.vehicle = vehicle
        self.slot = slot
        self.entry_time = entry_time
        self.exit_time = None

    def exit(self, exit_time):
        self.exit_time = exit_time
        return f"Vehicle {self.vehicle.license_plate} exited at {exit_time}"

class ParkingSystem:
    def __init__(self):
        self.slots = []
        self.tickets = []

    def add_slot(self, slot_id, slot_type):
        self.slots.append(Slot(slot_id, slot_type))

    def park_vehicle(self, license_plate, vehicle_type, slot_id):
        vehicle = Vehicle(license_plate, vehicle_type)
        for slot in self.slots:
            if slot.slot_id == slot_id and slot.is_available:
                slot.park(vehicle)
                ticket = Ticket(vehicle, slot, "10:00")
                self.tickets.append(ticket)
                return f"Vehicle {license_plate} parked in slot {slot_id}"
        return "Slot is not available"

    def leave_slot(self, slot_id):
        for slot in self.slots:
            if slot.slot_id == slot_id and not slot.is_available:
                return slot.leave()
        return "Slot is already empty"

    def get_ticket(self, license_plate):
        for ticket in self.tickets:
            if ticket.vehicle.license_plate == license_plate:
                return ticket
        return "Ticket not found"

parking_system = ParkingSystem()
parking_system.add_slot(1, "car")
parking_system.add_slot(2, "truck")
print(parking_system.park_vehicle("ABC123", "car", 1))
print(parking_system.park_vehicle("XYZ789", "truck", 2))
print(parking_system.leave_slot(1))
ticket = parking_system.get_ticket("ABC123")
print(ticket.exit("11:00"))