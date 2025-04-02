#include <iostream>
#include <math.h>
using namespace std;

class Vector
{
private:
double x;
double y;


public:
Vector()
{
  x = 0.0;
  y = 0.0;
}
Vector(double in_x,double in_y)
{
  x = in_x;
  y = in_y;
}
void SetX(double in_x)
{
  x =in_x;
}
void SetY(double in_y)
{
  y = in_y;
}
double GetX() const
{
  return x;
}
double GetY() const
{
  return y;
}
float magnitude()
{
  return sqrt(pow(x,2) + pow(y,2));
  
}
float angle()
{
  return atan(y/x);
}
float angleD()
{
  return (atan(y/x) * 180)/M_PI;
  
}
void multiply(double f)
{
  x = x*f;
  y = y*f;
}
Vector add(Vector v)
{
  Vector k;
  k.x = v.x + x;
  k.y = v.y + y;
  return k;
}
Vector clone()
{
  Vector c;
  c.x = x;
  c.y = y;
  return c;
}
};




