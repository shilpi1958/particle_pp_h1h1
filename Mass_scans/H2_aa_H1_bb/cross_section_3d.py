from __future__ import print_function
from ROOT import TCanvas, TGraph2D,gStyle
from ROOT import gROOT
from math import sin
from array import array


gStyle.SetPalette(1)
gStyle.SetMargin(0.1)

def SetCanvas():

    # CMS inputs
    # -------------
    H_ref = 2000;
    W_ref = 3000;
    W = W_ref
    H  = H_ref

    T = 0.08*H_ref
    B = 0.21*H_ref
    L = 0.12*W_ref
    R = 0.08*W_ref
    # --------------

    c1 = TCanvas("c2","c2",2000,1500)
    c1.SetFillColor(0)
    c1.SetBorderMode(0)
    c1.SetFrameFillStyle(0)
    c1.SetFrameBorderMode(0)
    c1.SetLeftMargin( L/W )
    c1.SetRightMargin( R/W )
    c1.SetTopMargin( T/H )
    c1.SetBottomMargin( B/H )
    c1.SetTickx(0)
    c1.SetTicky(0)
    c1.SetTickx(1)
    c1.SetTicky(1)
    c1.SetGridy()
    c1.SetGridx()
    #c1.SetLogy(1)
    return c1

c = SetCanvas()

gr = TGraph2D("graph.dat")
gr.SetTitle("Cross-Sections for H2_aa_H1_bb; H2 ; H3 ; Cross-Sections" )
gr.Draw( 'surf1' )
gr.Draw("same p0")

c.SaveAs("Cross-Sections for H2_aa_H1_bb.png" )
c.SaveAs("Cross-Sections for H2_aa_H1_bb.root")
