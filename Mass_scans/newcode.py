import ElementTree2 as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex
import os
import glob
import ROOT

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
#gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetHistFillStyle(2)


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

    c1 = TCanvas("c2","c2",5000,5000)
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


def CreateLegend(x1, y1, x2, y2, header):

    leg = ROOT.TLegend(x1, y1, x2, y2)
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

path = '/Users/chep/MG5_aMC_v2_6_5/h2aa_h1bb/Events/'

#H3_600GeV
runs=['01' , '04' ]
leg_entry=['M_{H2}=200, M_{H3}=600','M_{H2}=400, M_{H3}=600']

hists = [ [] for i in range(12) ]
graph = [ [] for i in range(12) ]
props = [ [] for i in range(12) ]

for i in runs:
    #massgamma
    graph[1]=TH1F('run_'+i,"H3(1MeV)",100,0,1000)
    #massbbbar
    graph[2]=TH1F('run_'+i,"H3(1MeV)",100,100,150)

    #h_b_pT
    graph[3]=TH1F('run_'+i,"H3(1MeV)",100,0,600)
    #h_b_eta
    graph[4]=TH1F('run_'+i,"H3(1MeV)",100,-5,5)
    #h_b_phi
    graph[5]=TH1F('run_'+i,"H3(1MeV)",10,-4,4)

    #h_bbar_pT
    graph[6]=TH1F('run_'+i,"H3(1MeV)",100,0,600)
    #h_bbar_eta
    graph[7]=TH1F('run_'+i,"H3(1MeV)",100,-5,5)
    #h_bbar_phi
    graph[8]=TH1F('run_'+i,"H3(1MeV)",10,-4,4)

    #h_a_pT
    graph[9]=TH1F('run_'+i,"H3(1MeV)", 100,0,600)
    #h_a_eta
    graph[10]=TH1F('run_'+i,"H3(1MeV)",100,-5,5)
    #h_a_phi
    graph[11]=TH1F('run_'+i,"H3(1MeV)",10,-4,4)


    files=glob.glob(path+'run_'+i+'/*.lhe')
    print (files)

    if files:
        tree=ET.parse(str(files[0]))
        root=tree.getroot()
        for child in root:
            if (child.tag=='event'):

                lines=child.text.strip().split('\n')
                event_header=lines[0].strip()
                num_part=int(event_header.split()[0].strip())
                if float (event_header.split()[2]) > 0:

                    a1_1=[s for s in lines if s.split()[0]=='22']
                    a1=a1_1[1::2]
                    a2=a1_1[0::2]
                    b=[s for s in lines if s.split()[0]=='5' ]
                    bbar=[s for s in lines if s.split()[0]=='-5']


                    if a1:
                        px1=float (a1[0].split()[6])
                        py1=float (a1[0].split()[7])
                        pz1=float (a1[0].split()[8])
                        e1=float (a1[0].split()[9])
                        p1=TLorentzVector(px1,py1,pz1,e1)

                    if a2:
                        px2=float (a2[0].split()[6])
                        py2=float (a2[0].split()[7])
                        pz2=float (a2[0].split()[8])
                        e2=float (a2[0].split()[9])
                        p2=TLorentzVector(px2,py2,pz2,e2)

                    if b:
                        px3=float (b[0].split()[6])
                        py3=float (b[0].split()[7])
                        pz3=float (b[0].split()[8])
                        e3=float (b[0].split()[9])
                        p3=TLorentzVector(px3,py3,pz3,e3)

                    if bbar:
                        px4=float (bbar[0].split()[6])
                        py4=float (bbar[0].split()[7])
                        pz4=float (bbar[0].split()[8])
                        e4=float (bbar[0].split()[9])
                        p4=TLorentzVector(px4,py4,pz4,e4)

                    #from gamma
                    HggP4=p1+p2

                    #from b bar
                    HbbP4=p3+p4

                    #props
                    #m_H1
                    props[1].append(HggP4.M())
                    #m_H2
                    props[2].append(HbbP4.M())

                    #b_pT
                    props[3].append(p3.Pt())
                    #b_eta
                    props[4].append(p3.Eta())
                    #b_phi
                    props[5].append(p3.Phi())

                    #bbar_pT
                    props[6].append(p4.Pt())
                    #bbar_eta
                    props[7].append(p4.Eta())
                    #bbar_phi
                    props[8].append(p4.Phi())

                    #a_pT
                    props[9].append(p1.Pt())
                    #a_eta
                    props[10].append(p1.Eta())
                    #a_phi
                    props[11].append(p1.Phi())

######################################################
for j, k,l in zip(range(len(graph)), range(len(hists)), range(len(props)) ):
    for i in props[l]:
            graph[j].Fill(i)
    hists[k].append(graph[j])
######################################################

attr = ['_MassGamma' , '_Massbbar' ,
        'phi_b', 'eta_b', '_pT_b'
        'phi_bbar', 'eta_bbar' , '_pT_bbar',
        'phi_a', 'eta_a', '_pT_a',]

ymax = [1, 1 ,
        1, 1, 1,
        1, 1, 1,
        1, 1, 1]

binwidth = [100, 100 ,
            100, 100, 100,
            100, 100, 100,
            100, 100, 100]

#############################################################
c      = SetCanvas()
legend = CreateLegend(0.78, 0.94, 0.93, 0.82, "")

print(len(hists[2]))

for i in range(len(hists)):
    for hist in range(len(hists[i])):
        print(hist)
        if hist==0:
            hists[i][hist].SetXTitle("M_{#gamma#gamma} [GeV]")
            hists[i][hist].SetYTitle("")
            hists[i][hist].SetLineColor(hist+1)
            hists[i][hist].SetLineWidth(3)
            hists[i][hist].SetLineStyle(hist+1)
            hists[i][hist].Scale(1/hists[i][hist].Integral())
            hists[i][hist].SetMaximum(ymax[i])
            #hists[i][hist].Rebin(binwidth[i])
            legend.AddEntry(hists[i][hist],leg_entry[hist],"L")
            hists[i][hist].Draw('hist')

        else:
            hists[i][hist].SetXTitle("M_{#gamma#gamma} [GeV]")
            hists[i][hist].SetYTitle("")
            hists[i][hist].SetLineColor(hist+1)
            hists[i][hist].SetLineWidth(3)
            hists[i][hist].SetLineStyle(hist+1)
            hists[i][hist].Scale(1/hists[i][hist].Integral())
            hists[i][hist].SetMaximum(ymax[i])
            #hists[i][hist].Rebin(binwidth[i])
            legend.AddEntry(hists[i][hist],leg_entry[hist],"L")
            hists[i][hist].Draw('hist')

    txt = '2HDM_NLO'
    texcms = AddText(txt)
    texCat= AddTextCat("pp_h3_h1h2_h1bb_h2aa")
    texcms.Draw("same")
    texCat.Draw("same")
    t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "", "")
    t.Draw('same')
    c.Update()

    legend.Draw()
    c.SaveAs("newCombined" + attr[i] + ".png" )
    c.SaveAs("newCombined" + attr[i] + ".root")













    x = [200, 400, 600 ,800]
    y = [ 600 ,800 ,1000]
    z = [3.920000e-33,
        2.538900e-33,
        1.908700e-33,
        2.350000e-33,
        1.400100e-33,
        8.429700e-34,
        0.000000e+00,
        9.294400e-34,
        7.454200e-34,
        0.000000e+00,
        0.000000e+00,
        4.527300e-34]
