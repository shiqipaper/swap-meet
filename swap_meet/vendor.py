from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
                    # Wave_2 

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    

                    #wave_3
    
    def swap_items(self, other_vendor, my_item, their_item):

        if not my_item in self.inventory or not their_item in other_vendor.inventory:
            return False
        

        self.remove(my_item) #removes `my_item` from this `Vendor`'s inventory
        other_vendor.add(my_item) #adds it to the friend's inventory
        self.add(their_item) #adds it to this `Vendor`'s inventory
        other_vendor.remove(their_item) #removes `their_item` from the other `Vendor`'s inventory

        return True
    

                    # Wave_4

    def swap_first_item(self, other_vendor):

        if not self.inventory or not other_vendor.inventory:
            return False
        
        # Remove the first item from both vendors' inventories
        self_first_item  = self.inventory.pop(0)
        others_first_item = other_vendor.inventory.pop(0)

        # Add the first item from the other vendor to each vendor's inventory
        self.inventory.insert(0, others_first_item)
        other_vendor.inventory.insert(0,self_first_item)

        # Return True to indicate the swap was successful
        return True
    

                    # Wave_6
    def get_by_category(self, category):
        list_of_objects = []
        for item in self.inventory:
            if category == item.get_category():
                list_of_objects.append(item)
        return list_of_objects
        

    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None
        
        best_item = self.get_by_category(category)[0]
        for item in self.get_by_category(category):
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory: 
            return False

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        
        if my_best_item.get_category() == their_priority and their_best_item.get_category() == my_priority:
            other_vendor.add(my_best_item)
            self.remove(my_best_item)
            self.add(their_best_item)
            other_vendor.remove(their_best_item)
            return True





