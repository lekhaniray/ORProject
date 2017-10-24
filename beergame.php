<?php

$N=$_post['weeks'];
$customer_lower=$_post['Retailer_lower'];
$customer_upper=$_post['Retailer_upper'];
$ad=$_post['change'];
$customer_upper_new = $customer_upper + $ad;
$customer_lower_new = $customer_lower + $ad;

// Initialization
$Orders_C = array_fill(0,1, array_fill(0, N,0));
$Orders_R = array_fill(0,1, array_fill(0, N,0));
$Orders_W = array_fill(0,1, array_fill(0, N,0));
$Orders_D = array_fill(0,1, array_fill(0, N,0));
$Orders_F = array_fill(0,1, array_fill(0, N,0));

$Total_cost_R_array = array_fill(0,1, array_fill(0, N,0)); 
$Total_cost_W_array = array_fill(0,1, array_fill(0, N,0)); 
$Total_cost_D_array = array_fill(0,1, array_fill(0, N,0)); 
$Total_cost_F_array = array_fill(0,1, array_fill(0, N,0));

$Total_stock_R = array_fill(0,1, array_fill(0, N,0)); 
$Total_stock_W = array_fill(0,1, array_fill(0, N,0)); 
$Total_stock_D = array_fill(0,1, array_fill(0, N,0)); 
$Total_stock_F = array_fill(0,1, array_fill(0, N,0));

$My_Order_R = array_fill(0,1, array_fill(0, N,0)); 
$My_Order_W = array_fill(0,1, array_fill(0, N,0)); 
$My_Order_D = array_fill(0,1, array_fill(0, N,0)); 
$My_Order_F = array_fill(0,1, array_fill(0, N,0));

$Outgoing_Deliv_W = array_fill(0,1, array_fill(0, N+10,0)); 
$Outgoing_Deliv_D = array_fill(0,1, array_fill(0, N+10,0)); 
$Outgoing_Deliv_F = array_fill(0,1, array_fill(0, N+10,0));

$Backorder_R = 0;
$Stock_R = $_post['iRetailer'];
$Incoming_Deliv_R = 0;
$Backorder_W = 0;
$Stock_W = $_post['iWholeseller'];
$Incoming_Deliv_W = 0;
$Backorder_D = 0;
$Stock_D = $_post['iDistributor'];
$Incoming_Deliv_D = 0;
$Backorder_F = 0;
$Stock_F = $_post['iFactory'];
$Incoming_Deliv_F = 0;
$Init_order = $_post['iOrder'];

// Bullwhip Simulator
for(i=1;i<N;i++)
{
	echo $i;
	if ($i<=5) 
	{
        $Customer_Demand = rand($customer_lower, $customer_upper);   //Random   Customer   Demand   
	}
	else
    {
    	$Customer_Demand = rand($customer_lower+$ad, $customer_upper+$ad);
    }

    echo ("RETAILER:")           
    if($i<=2)
    {
     	$Incoming_Deliv_R = 0;
    }
    else
    {
    	$Incoming_Deliv_R = $Outgoing_Deliv_W($i-2);
    }
                                
}
843301075995
?>