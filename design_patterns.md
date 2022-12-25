# Problems
## Coupling
- the degree of interdependence between module. a measure of how closely connected two routines or modules are

# Solutions
## Coupling
- avoid deep inheritance relationships
- seperate creating resources from using them
- introduce abstraction
- avoid inappropriate intimacy
- introduce an intermediate DS


Look into enum auto, using abstract methods

- isinstance point to a deeper problem in your code. you didn't think carefully about how the responsibilities in your code are distributed. a method that uses isInstance should instead be made into a method of the instances it checks. This makes it so no checking is needed and instead the inheritance hierachy handles that
- boolean flags to functions actually show that a function does too many things. this is bad because a method should divy out responsibilities