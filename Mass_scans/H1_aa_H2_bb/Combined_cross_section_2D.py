from ROOT import TCanvas,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, gROOT, TNamed, TLegend, gStyle, TGraph
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math

def SetCanvas():

    # CMS inputs
    # -------------
    H_ref = 1000;
    W_ref = 1000;
    W = W_ref
    H  = H_ref

    T = 0.08*H_ref
    B = 0.21*H_ref
    L = 0.12*W_ref
    R = 0.08*W_ref
    # --------------

    c1 = TCanvas("c2","c2",0,0,2000,1500)
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
    c1.SetGridy(1)
    c1.SetGridx(1)
    c1.SetLogy(0)
    return c1

def CreateLegend(x1, y1, x2, y2, header):

    leg = ROOT.TLegend(x1, x2, y1, y2)
    leg.SetFillColor(0)
    leg.SetFillStyle(3002)
    leg.SetBorderSize(0)
    leg.SetHeader(header)
    return leg


def AddText(txt):
    texcms = ROOT.TLatex(-20.0, 50.0, txt)
    texcms.SetNDC()
    texcms.SetTextAlign(12)
    texcms.SetX(0.1)
    texcms.SetY(0.94)
    texcms.SetTextSize(0.02)
    texcms.SetTextSizePixels(22)
    return texcms

def AddTextCat(cat):
    texCat = ROOT.TLatex(-20.0, 50.0, cat)
    texCat.SetNDC()
    texCat.SetTextAlign(12)
    texCat.SetX(0.85)
    texCat.SetY(0.94)
    texCat.SetTextFont(40)
    texCat.SetTextSize(0.025)
    texCat.SetTextSizePixels(22)
    return texCat


leg_entry=['M_{A0}=300 GeV','M_{A0}=400 GeV','M_{A0}=500 GeV']
runs=["300","400","500"]
c =SetCanvas()
gStyle.SetPalette(1)
legend = CreateLegend(0.70, 0.94, 0.75, 0.92, "m_{h}=125 GeV")

dt =TGraph("H3_600GeV.dat")
dt.SetTitle("Cross-Sections for H3 -> H1 (#gamma #gamma) H2 (b b~) ; M_{H2} [GeV] ; Cross-Sections [pb")
dt.SetLineColor(2)
dt.SetLineWidth(4)
dt.Draw("ACP*")
legend.AddEntry(dt,'m_{H3}=600 GeV',"L")

dt1 =TGraph("H3_800GeV.dat")
dt1.SetTitle("Cross-Sections for H3 -> H1 (#gamma #gamma) H2 (b b~) ; M_{H2} [GeV] ; Cross-Sections [pb")
dt1.SetLineColor(3)
dt1.SetLineWidth(4)
dt1.Draw("CP*")
legend.AddEntry(dt1,'m_{H3}=800 GeV',"L")

dt2 =TGraph("H3_1000GeV.dat")
dt2.SetTitle("Cross-Sections for H3 -> H1 (#gamma #gamma) H2 (b b~) ; M_{H2} [GeV] ; Cross-Sections [pb")
dt2.SetLineColor(4)
dt2.SetLineWidth(4)
dt2.Draw("CP*")
legend.AddEntry(dt2,'m_{H3}=1000 GeV',"L")

legend.Draw("same")
# for i in range(len(runs)):
#     dt =TGraph("Graph_a0_"+runs[i]+".dat")
#     dt.SetTitle("Combined Cross-section for Zp->A0(bb~) h(#gamma#gamma); m_{zp}[GeV]; Cross-section[pb]")
#     if i==0:
#         dt.SetLineColor(i+1)
#         dt.SetLineWidth(3)
#         dt.Draw("AC*")
#
#     else:
#         dt.SetLineColor(i+1)
#         dt.SetLineWidth(3)
#         dt.Draw("CP*")

c.SaveAs("Combined_cross_section_2D.png")
c.SaveAs("Combined_cross_section_2D.root")
