class Category:

    def __init__(self, s):
        self.ledger = list()
        self.funds = 0
        self.name = s
        self.spent = 0

    def __str__(self):
        s = "{:*^30}".format(self.name) + "\n"

        for i in self.ledger:
            s = s + "{:23.23}".format(i["description"]) + "{:7.2f}".format(i["amount"]) + "\n"

        s = s + "Total: " + "{:.2f}".format(self.funds)
        
        return s    

    def get_balance(self):
        return self.funds;

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def deposit(self, x, dis = ""):
        d = dict()
        d["amount"] = x
        d["description"] = dis

        self.ledger.append(d)
        self.funds = self.funds + x
    
    def withdraw(self, x, dis = ""):
        if self.check_funds(x):
            self.deposit(-x, dis)
            self.spent = self.spent + x
        
        return self.check_funds(x)
    
    def transfer(self, x, ob):
        if self.withdraw(x, f"Transfer to {ob.name}"):
            ob.deposit(x, f"Transfer from {self.name}")
            return True
        
        return False



def create_spend_chart(categories):
    mx = 0
    total = 0;

    for i in categories:
        mx = max(mx, len(i.name))
        total = total + i.spent
    
  
    s = list()
    temp = "{:<{}s}".format("1", 12 + mx)
    s.append(temp)
    temp = "{:<{}s}".format("0987654321", 12 + mx)
    s.append(temp)
    temp = "{:0<11}".format("") + "{:<{}s}".format("",1 + mx)
    s.append(temp)
    temp = "{:|<11}".format("") + "{:<{}s}".format("",1 + mx)
    s.append(temp)
    temp = "{:<11}".format("") + "{:<{}s}".format("-",1 + mx)
    s.append(temp)

    space = "{:11}".format("") + "-" + "{:{}s}".format("",mx)

    for i in categories:
        bar = int((i.spent/total)*10.0) + 1
       
        ttemp = "{:o<{}s}".format("",bar)
        
        temp = "{:>11}".format(ttemp) + "-" + "{:{}s}".format(i.name, mx)
        s.append(temp)
        s.append(space)
        s.append(space)

    res = "Percentage spent by category\n"
    for i in range(12+mx):
        for j in s:
            res = res + j[i]
        res = res + "\n"
  
    res = res[:len(res)-1]
    return res

