

print "The Bullwhip effect simulated"
print "Welcome to the Beer Distribution Game"


N = input("Enter the number of games you want to play")
array = input("Define the random customer demand between interval")
ad = input("Define the random change")


    #--------------------- Various Initializations-----------------------%
    Orders_C = zeros(1, N)
    Orders_R = zeros(1, N)
    Orders_W = zeros(1, N)
    Orders_D = zeros(1, N)
    Orders_F = zeros(1, N)
    Total_cost_R_array = zeros(1, N)
    Total_cost_W_array = zeros(1, N)
    Total_cost_D_array = zeros(1, N)
    Total_cost_F_array = zeros(1, N)
    Total_stock_R = zeros(1, N)
    Total_stock_W = zeros(1, N)
    Total_stock_D = zeros(1, N)
    Total_stock_F = zeros(1, N)
    My_Order_R = zeros(1, N)
    My_Order_W = zeros(1, N)
    My_Order_D = zeros(1, N)
    My_Order_F = zeros(1, N)
    Outgoing_Deliv_W = zeros(1, N + 10)
    Outgoing_Deliv_D = zeros(1, N + 10)
    Outgoing_Deliv_F = zeros(1, N + 10)
    Backorder_R = 0
    Stock_R = input("What is your initial stock Retailer")
    Incoming_Deliv_R = 0
    Backorder_W = 0
    Stock_W = input("What is your initial stock Wholesaler")
    Incoming_Deliv_W = 0
    Backorder_D = 0
    Stock_D = input("What is your initial stock Distributor")
    Incoming_Deliv_D = 0
    Backorder_F = 0
    Stock_F = input("What is your initial stock Factory")
    Incoming_Deliv_F = 0
   init_order=input("What is the initial quatity of orders")


    #--------------------- The bullwhip simulator ----------------------%
    for i in mslice[1:N]:
		print"%d" %i

        if (i <= 5):        #--- After 5 rounds the Customer Demand is going to increase according to the
            additive(mstring('value'), mstring(':ad'))
            Customer_Demand = randi(mcat([array(1), array(2)]))        #---Random Customer Demand between the
            interval(mstring('of'), mstring('10'), mstring('and'), mstring('20'))
        else:
            Customer_Demand = randi(mcat([array(1) + ad, array(2) + ad]))        #--- The random change in Customer
            Demand(mstring('that'), mstring('causes'), mstring('the'), mstring('bullwhip'), mstring('effect.'))
            end
            #-- Retailer ---%
            disp(mstring(' RETAILER: '))
            if (i <= 2):
                Incoming_Deliv_R = 0
            else:
                Incoming_Deliv_R = Outgoing_Deliv_W(i - 2)
                end
                Incoming_Order_R = Customer_Demand            #---- Order from Customer
                c_R = (Stock_R + Incoming_Deliv_R) - (Incoming_Order_R + Backorder_R)
                if (c_R < 0):
                    Outgoing_Deliv_R = Stock_R + Incoming_Deliv_R
                    Backorder_R = abs(c_R)
                    Stock_R = 0
                else:
                    Outgoing_Deliv_R = Incoming_Order_R + Backorder_R
                    Stock_R = c_R
                    Backorder_R = 0
                    end
                    Total_cost_R = Backorder_R * 2 + Stock_R * 1
                    Total_cost_R_array(i).lvalue = Total_cost_R
                    if (Stock_R > 0):
                        Total_stock_R(i).lvalue = Stock_R
                    else:
                        Total_stock_R(i).lvalue = -Backorder_R
                        end
                        Orders_C(i).lvalue = Incoming_Order_R
                        disp(mstring('Incoming Delivery from provider: '))
                        fprintf(mstring('%d'), Incoming_Deliv_R)
                        fprintf(mstring('\\n'))
                        disp(mstring('Incoming Order from client: '))
                        fprintf(mstring('%d'), Incoming_Order_R)
                        fprintf(mstring('\\n'))
                        disp(mstring('Outgoing Delivery: '))
                        fprintf(mstring('%d'), Outgoing_Deliv_R)
                        fprintf(mstring('\\n'))
                        disp(mstring('Backorder: '))
                        fprintf(mstring('%d'), Backorder_R)
                        fprintf(mstring('\\n'))
                        disp(mstring('Stock: '))
                        fprintf(mstring('%d'), Stock_R)
                        fprintf(mstring('\\n'))
                        disp(mstring('Total cost: '))
                        fprintf(mstring('%d'), Total_cost_R)
                        fprintf(mstring('\\n'))
                        My_Order_R(i).lvalue = input(mstring('Whats your order Retailer ?: '))
                        Orders_R(i).lvalue = My_Order_R(i)
                       
                        fprintf(mstring('\\n'))
                        fprintf(mstring('\\n'))
                        fprintf(mstring('\\n'))

                        #-- Wholesaler ---%
                        disp(mstring(' WHOLESALER: '))
                        if (i <= 2):
                            Incoming_Deliv_W = 0
                        else:
                            Incoming_Deliv_W = Outgoing_Deliv_D(i - 2)
                            end
                            if (i == 1):
                                Incoming_Order_W = Init_order
                            else:
                                Incoming_Order_W = My_Order_R(i - 1)                            #---- Order from retailer
                                end
                                c_W = (Stock_W + Incoming_Deliv_W) - (Incoming_Order_W + Backorder_W)
                                if (c_W < 0):
                                    Outgoing_Deliv_W(i).lvalue = Stock_W + Incoming_Deliv_W
                                    Backorder_W = abs(c_W)
                                    Stock_W = 0
                                else:
                                    Outgoing_Deliv_W(i).lvalue = Incoming_Order_W + Backorder_W
                                    Stock_W = c_W
                                    Backorder_W = 0
                                    end
                                    Total_cost_W = Backorder_W * 2 + Stock_W * 1
                                    Total_cost_W_array(i).lvalue = Total_cost_W
                                    if (Stock_W > 0):
                                        Total_stock_W(i).lvalue = Stock_W
                                    else:
                                        Total_stock_W(i).lvalue = -Backorder_W
                                        end
                                        disp(mstring('Incoming Delivery from provider: '))
                                        fprintf(mstring('%d'), Incoming_Deliv_W)
                                        fprintf(mstring('\\n'))
                                        disp(mstring('Incoming Order from client: '))
                                        fprintf(mstring('%d'), Incoming_Order_W)
                                        fprintf(mstring('\\n'))
                                        disp(mstring('Outgoing Delivery: '))
                                        fprintf(mstring('%d'), Outgoing_Deliv_W(i))
                                        fprintf(mstring('\\n'))
                                        disp(mstring('Backorder: '))
                                        fprintf(mstring('%d'), Backorder_W)
                                        fprintf(mstring('\\n'))
                                        disp(mstring('Stock: '))
                                        fprintf(mstring('%d'), Stock_W)
                                        fprintf(mstring('\\n'))
                                        disp(mstring('Total cost: '))
                                        fprintf(mstring('%d'), Total_cost_W)
                                        fprintf(mstring('\\n'))
                                        My_Order_W(i).lvalue = input(mstring('Whats your order wholesaler ?: '))
                                        Orders_W(i).lvalue = My_Order_W(i)
                                     
                                        fprintf(mstring('\\n'))
                                        fprintf(mstring('\\n'))
                                        fprintf(mstring('\\n'))

                                        #-- Distributor ---%
                                        disp(mstring(' DSTRIBUTOR: '))
                                        if (i <= 2):
                                            Incoming_Deliv_D = 0
                                        else:
                                            Incoming_Deliv_D = Outgoing_Deliv_F(i - 2)
                                            end
                                            if (i == 1):
                                                Incoming_Order_D = Init_order
                                            else:
                                                Incoming_Order_D = My_Order_W(i - 1)                                            #---- Order from Wholesaler
                                                end
                                                c_D = (Stock_D + Incoming_Deliv_D) - (Incoming_Order_D + Backorder_D)
                                                if (c_D < 0):
                                                    Outgoing_Deliv_D(i).lvalue = Stock_D + Incoming_Deliv_D
                                                    Backorder_D = abs(c_D)
                                                    Stock_D = 0
                                                else:
                                                    Outgoing_Deliv_D(i).lvalue = Incoming_Order_D + Backorder_D
                                                    Stock_D = c_D
                                                    Backorder_D = 0
                                                    end
                                                    Total_cost_D = Backorder_D * 2 + Stock_D * 1
                                                    Total_cost_D_array(i).lvalue = Total_cost_D
                                                    if (Stock_D > 0):
                                                        Total_stock_D(i).lvalue = Stock_D
                                                    else:
                                                        Total_stock_D(i).lvalue = -Backorder_D
                                                        end
                                                        disp(mstring('Incoming Delivery from provider: '))
                                                        fprintf(mstring('%d'), Incoming_Deliv_D)
                                                        fprintf(mstring('\\n'))
                                                        disp(mstring('Incoming Order from client: '))
                                                        fprintf(mstring('%d'), Incoming_Order_D)
                                                        fprintf(mstring('\\n'))
                                                        disp(mstring('Outgoing Delivery: '))
                                                        fprintf(mstring('%d'), Outgoing_Deliv_D(i))
                                                        fprintf(mstring('\\n'))
                                                        disp(mstring('Backorder: '))
                                                        fprintf(mstring('%d'), Backorder_D)
                                                        fprintf(mstring('\\n'))
                                                        disp(mstring('Stock: '))
                                                        fprintf(mstring('%d'), Stock_D)
                                                        fprintf(mstring('\\n'))
                                                        disp(mstring('Total cost: '))
                                                        fprintf(mstring('%d'), Total_cost_D)
                                                        fprintf(mstring('\\n'))
                                                        My_Order_D(i).lvalue = input(mstring('Whats your order distributor ?: '))
                                                        Orders_D(i).lvalue = My_Order_D(i)
                                                       
                                                        fprintf(mstring('\\n'))
                                                        fprintf(mstring('\\n'))
                                                        fprintf(mstring('\\n'))

                                                        #--- Factory ---%
                                                        disp(mstring(' FACTORY: '))
                                                        if (i <= 3):
                                                            Incoming_Deliv_F = 0
                                                        else:
                                                            Incoming_Deliv_F = My_Order_F(i - 3)
                                                            end
                                                            if (i == 1):
                                                                Incoming_Order_F = Init_order
                                                            else:
                                                                Incoming_Order_F = My_Order_D(i - 1)                                                            #---- Order from Distributor
                                                                end
                                                                c_F = (Stock_F + Incoming_Deliv_F) - (Incoming_Order_F + Backorder_F)
                                                                if (c_F < 0):
                                                                    Outgoing_Deliv_F(i).lvalue = Stock_F + Incoming_Deliv_F
                                                                    Backorder_F = abs(c_F)
                                                                    Stock_F = 0
                                                                else:
                                                                    Outgoing_Deliv_F(i).lvalue = Incoming_Order_F + Backorder_F
                                                                    Stock_F = c_F
                                                                    Backorder_F = 0
                                                                    end
                                                                    Total_cost_F = Backorder_F * 2 + Stock_F * 1
                                                                    Total_cost_F_array(i).lvalue = Total_cost_F
                                                                    if (Stock_F > 0):
                                                                        Total_stock_F(i).lvalue = Stock_F
                                                                    else:
                                                                        Total_stock_F(i).lvalue = -Backorder_F
                                                                        end
                                                                        disp(mstring('Incoming Delivery from provider: '))
                                                                        fprintf(mstring('%d'), Incoming_Deliv_F)
                                                                        fprintf(mstring('\\n'))
                                                                        disp(mstring('Incoming Order from client: '))
                                                                        fprintf(mstring('%d'), Incoming_Order_F)
                                                                        fprintf(mstring('\\n'))
                                                                        disp(mstring('Outgoing Delivery: '))
                                                                        fprintf(mstring('%d'), Outgoing_Deliv_F(i))
                                                                        fprintf(mstring('\\n'))
                                                                        disp(mstring('Backorder: '))
                                                                        fprintf(mstring('%d'), Backorder_F)
                                                                        fprintf(mstring('\\n'))
                                                                        disp(mstring('Stock: '))
                                                                        fprintf(mstring('%d'), Stock_F)
                                                                        fprintf(mstring('\\n'))
                                                                        disp(mstring('Total cost: '))
                                                                        fprintf(mstring('%d'), Total_cost_F)
                                                                        fprintf(mstring('\\n'))
                                                                        My_Order_F(i).lvalue = input(mstring('Whats your order factory ?: '))
                                                                        Orders_F(i).lvalue = My_Order_F(i)
                                                                      
                                                                        fprintf(mstring('\\n'))
                                                                        fprintf(mstring('\\n'))
                                                                        fprintf(mstring('\\n'))

                                                                        #----------------------------------------------------------------%
                                                                        end
                                                                        weeks = mslice[1:N]
                                                                        # -- Plot of the Total Cost of every department during the week time
                                                                        figure()
                                                                        p1 = plot(weeks, Total_cost_R_array)
                                                                        title(mstring('Plot of Total Department Cost'))
                                                                        xlabel(mstring('Weeks'))
                                                                        ylabel(mstring('Total Cost'))
                                                                        set(p1, mstring('Color'), mstring('b'))
                                                                        hold(mstring('on'))
                                                                        p2 = plot(weeks, Total_cost_W_array)
                                                                        set(p2, mstring('Color'), mstring('g'))
                                                                        hold(mstring('on'))
                                                                        p3 = plot(weeks, Total_cost_D_array)
                                                                        set(p3, mstring('Color'), mstring('y'))
                                                                        hold(mstring('on'))
                                                                        p4 = plot(weeks, Total_cost_F_array)
                                                                        set(p4, mstring('Color'), mstring('r'))
                                                                        legend(mstring('Retailer'), mstring('Wholesaler'), mstring('Distributor'), mstring('Factory'))
                                                                        # -- Plot of the Total Stock in every department during the week time
                                                                        figure()
                                                                        p1 = plot(weeks, Total_stock_R)
                                                                        title(mstring('Plot of Total Stocks'))
                                                                        xlabel(mstring('Weeks'))
                                                                        ylabel(mstring('Stocks'))
                                                                        set(p1, mstring('Color'), mstring('b'))
                                                                        hold(mstring('on'))
                                                                        p2 = plot(weeks, Total_stock_W)
                                                                        set(p2, mstring('Color'), mstring('g'))
                                                                        hold(mstring('on'))
                                                                        p3 = plot(weeks, Total_stock_D)
                                                                        set(p3, mstring('Color'), mstring('y'))
                                                                        hold(mstring('on'))
                                                                        p4 = plot(weeks, Total_stock_F)
                                                                        set(p4, mstring('Color'), mstring('r'))
                                                                        legend(mstring('Retailer'), mstring('Wholesaler'), mstring('Distributor'), mstring('Factory'))
                                                                        # -- Plot of the Total Orders in every department during the week time
                                                                        figure()
                                                                        p1 = plot(weeks, Orders_C)
                                                                        title(mstring('Plot of Total Orders'))
                                                                        xlabel(mstring('Weeks'))
                                                                        ylabel(mstring('Orders'))
                                                                        set(p1, mstring('Color'), mstring('black'))
                                                                        hold(mstring('on'))
                                                                        p2 = plot(weeks, Orders_R)
                                                                        set(p2, mstring('Color'), mstring('b'))
                                                                        hold(mstring('on'))
                                                                        p3 = plot(weeks, Orders_W)
                                                                        set(p3, mstring('Color'), mstring('g'))
                                                                        hold(mstring('on'))
                                                                        p4 = plot(weeks, Orders_D)
                                                                        set(p4, mstring('Color'), mstring('y'))
                                                                        p4 = plot(weeks, Orders_F)
                                                                        set(p4, mstring('Color'), mstring('r'))
                                                                        legend(mstring('Customer'), mstring('Retailer'), mstring('Wholesaler'), mstring('Distributor'), mstring('Factory'))
                                                                        #-- The end :-)... !!!

