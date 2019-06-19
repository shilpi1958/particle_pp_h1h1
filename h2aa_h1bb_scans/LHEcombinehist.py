import ElementTree2 as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex
import os
import glob

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
gStyle.SetLegendBorderSize(0)
#gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetHistFillStyle(2)

path = '/Users/chep/MG5_aMC_v2_6_5/h2aa_h1bb/Events/'

runs=['01','02','03','04','05','06','07','08']

hists1=[]
hists2=[]

for i in runs:
    m_H1=[]
    m_H2=[]
    m_H3=[]
    pT=[]
    eta=[]
    phi=[]
    #mass=[]
    h_m_H1=TH1F('run_'+i,"",10000,0,200)
    h_m_H2=TH1F('run_'+i,"",10000,0,800)
    files=glob.glob(path+'run_'+i+'/*.lhe')
    print (files)
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

                HggP4=p1+p2
                HbbP4=p3+p4
                m_H1.append(HggP4.M())
                m_H2.append(HbbP4.M())

    for mass in m_H1:
            h_m_H1.Fill(mass)
    hists1.append(h_m_H1)

    for i in m_H2:
        h_m_H2.Fill(i)
    hists2.append(h_m_H2)

c=TCanvas("c1","",1500,2000)
c.SetLogy()
#print len(hists1)

for hist in range(len(hists1)):
    print hist
    if hist==0:
        hists1[hist].SetXTitle("M_{#gamma#gamma} [GeV]")
        hists1[hist].SetYTitle("Events")
        hists1[hist].SetLineColor(hist+1)
        #hists1[hist].Rebin(5)
        hists1[hist].SetLineWidth(3)
        hists1[hist].SetMaximum(2)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists1[hist].DrawNormalized('hist')

    else:
        hists1[hist].SetXTitle("M_{#gamma#gamma} [GeV]")
        hists1[hist].SetYTitle("Events")
        hists1[hist].SetLineColor(hist+1)
        #hists1[hist].Rebin(5)
        hists1[hist].SetLineWidth(3)
        hists1[hist].SetMaximum(2)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists1[hist].DrawNormalized('hist&same')

#cmsname.Draw()
#legend.Draw()

c.SaveAs("CombinedMass.png")
c.SaveAs("CombinedMass.root")


#############################################################

for hist in range(len(hists2)):
    print hist
    if hist==0:
        hists2[hist].SetXTitle("M_{bb~} [GeV]")
        hists2[hist].SetYTitle("Events")
        hists2[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(2)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists2[hist].DrawNormalized('hist')

    else:
        hists2[hist].SetXTitle("M_{bb~} [GeV]")
        hists2[hist].SetYTitle("Events")
        hists2[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(2)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists2[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedMassbb~.png")
c.SaveAs("CombinedMassbb~.root")
