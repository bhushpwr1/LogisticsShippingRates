# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kolograms: "))
rate =float(input("Enter the shipping rate per kilogram: "))

## Calculate Shipping Cost
shipping_cost = weight * rate

## Display the results
print(f"shipping cost: {shipping_cost} USD")
