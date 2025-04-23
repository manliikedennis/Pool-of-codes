#weight of shiiping an item
weight = 41.5
#premium cost of shipping that item
premium_ground_shipping = 125
#ground shipping calculations for shipping
if weight <= 2:
  ground_cost = weight * 1.5 + 20
elif weight >= 2 and weight <= 6:
  ground_cost = weight * 3 + 20
elif weight >= 6 and weight <= 10:
  ground_cost = weight * 4 + 20
else:
  ground_cost = weight * 4.75 + 20

print(ground_cost)
print("Cost of ground shipping: ", premium_ground_shipping)

drone_weight = 41.5
#Drone shipping section
if drone_weight <= 2:
  drone_shipping_cost = drone_weight * 4.50
elif drone_weight > 2 and drone_weight <= 6:
  drone_shipping_cost = drone_weight * 9
elif drone_weight > 6 and drone_weight <= 10:
  drone_shipping_cost = drone_weight * 12
else:
  drone_shipping_cost = drone_weight * 14.25

print(drone_shipping_cost)

if ground_cost < premium_ground_shipping and ground_cost < drone_shipping_cost:
    print("Ground shipping is cheapest: $", ground_cost)
elif premium_ground_shipping < ground_cost and premium_ground_shipping < drone_shipping_cost:
    print("Premium ground shipping is cheapest: $", premium_ground_shipping)
else:
    print("Drone shipping is cheapest: $", drone_shipping_cost)
