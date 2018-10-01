from ROOT import gROOT, TCanvas, TF2

gROOT.Reset()
c1 = TCanvas( 'c1', 'Sin(x) * Cos(y)', 200, 10, 700, 500 )

#
# Create a one dimensional function and draw it
#
f1 = TF2("f1", "sin(x) * cos (y)", 0, 10, 0 , 10)
c1.SetGridx()
c1.SetGridy()
f1.Draw()
c1.Update()
