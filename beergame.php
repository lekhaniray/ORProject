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
for($i=1;i<N;$i++)
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
    
    $Incoming_Order_R = $Customer_Demand;   // Order from Customer
    $c_R = ($Stock_R + $Incoming_Deliv_R) - ($Incoming_Order_R + $Backorder_R);           
    if($c_R<0)
    {
        $Outgoing_Deliv_R = $Stock_R + $Incoming_Deliv_R;
        $Backorder_R = abs($c_R);
        $Stock_R=0;
    }
    else
    {
        $Outgoing_Deliv_R = $Incoming_Order_R + $Backorder_R;                       
        $Stock_R = $c_R;
        $Backorder_R = 0;
    }

    $Total_cost_R = $Backorder_R * 2 + $Stock_R * 1;           
    $Total_cost_R_array($i) = $Total_cost_R;
    if($Stock_R > 0)
    {
        $Total_stock_R($i) = $Stock_R;
    }
    else
    {
        $Total_stock_R($i) = - $Backorder_R;
    }           
    $Orders_C($i) = $Incoming_Order_R;
    
    echo ("Incoming Delivery from provider: ");           
    echo $Incoming_Deliv_R;
    echo "<br>";
    echo ("Incoming Order from client: ");
    echo $Incoming_Order_R;
    echo ("Outgoing   Delivery: ");
    echo $Outgoing_Deliv_R;
    echo "<br>";
    echo ("Backorder: ");
    echo $Backorder_R;
    echo "<br>";
    echo ("Stock: ");
    echo $Stock_R;
    echo "<br>"
    echo ("Total   cost: ");
    echo $Total_cost_R;
    echo "<br>";
    $My_Order_R($i) = $_post['Retailer_order'];          
    $Orders_R($i) = $My_Order_R($i);
    echo "<br>"; echo "<br>"; echo "<br>";

    // Wholesaler 
    echo ("WHOLESALER: ");
    if($i < = 2)
    {
        $Incoming_Deliv_W = 0;
    }
    else
    {
        $Incoming_Deliv_W = $Outgoing_Deliv_D ($i - 2);
    }

    if($i == 1)
    {
        $Incoming_Order_W = $Init_order;
    }
    else
    {
        $Incoming_Order_W = $My_Order_R($i-1);   // Order   from   retailer
    }           
    $c_W = ($Stock_W + $Incoming_Deliv_W) - ($Incoming_Order_W + $Backorder_W);           
    if($c_W < 0)
    {
        $Outgoing_Deliv_W($i) = $Stock_W + $Incoming_Deliv_W;
        $Backorder_W = abs($c_W);
        $Stock_W = 0;
    }    
    else
    {
        $Outgoing_Deliv_W($i) = $Incoming_Order_W + $Backorder_W;                       
        $Stock_W = $c_W;
        $Backorder_W=0;
    } 
          
    $Total_cost_W = $Backorder_W*2 + $Stock_W*1;           
    $Total_cost_W_array($i) = $Total_cost_W;
    if($Stock_W > 0)
    {
        $Total_stock_W($i) = $Stock_W;
    }
    else
    {
        $Total_stock_W($i) =- $Backorder_W;
    }          
    echo("Incoming Delivery from provider: ");           
    echo $Incoming_Deliv_W;
    echo "<br>";
    echo("Incoming   Order   from   client: ");
    echo $Incoming_Order_W;           
    echo "<br>";
    echo("Outgoing Delivery: ");
    echo $Outgoing_Deliv_W($i);           
    echo "<br>";
    echo("Backorder: ");
    echo $Backorder_W;
                                 
}
?>