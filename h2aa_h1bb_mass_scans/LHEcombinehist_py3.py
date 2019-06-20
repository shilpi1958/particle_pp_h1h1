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

runs=['01' ,'02','03','04','05','06','08' , '09', '12']

hists1=[]
hists2=[]

hists3=[]
hists4=[]
hists5=[]

hists6=[]
hists7=[]
hists8=[]

hists9=[]
hists10=[]
hists11=[]

for i in runs:
    m_H1=[]
    m_H2=[]
    m_H3=[]

    b_pT=[]
    b_eta=[]
    b_phi=[]

    bbar_pT=[]
    bbar_eta=[]
    bbar_phi=[]

    a_pT=[]
    a_eta=[]
    a_phi=[]

    #mass=[]
    h_m_H1=TH1F('run_'+i,"",100,0,1000)
    h_m_H2=TH1F('run_'+i,"",100,100,150)

    h_b_pT=TH1F('run_'+i,"",100,0,1000)
    h_b_eta=TH1F('run_'+i,"",100,-5,5)
    h_b_phi=TH1F('run_'+i,"",10,-4,4)

    h_bbar_pT=TH1F('run_'+i,"",100,0,1000)
    h_bbar_eta=TH1F('run_'+i,"",100,-5,5)
    h_bbar_phi=TH1F('run_'+i,"",10,-4,4)

    h_a_pT=TH1F('run_'+i,"", 100,0,1000)
    h_a_eta=TH1F('run_'+i,"",100,-5,5)
    h_a_phi=TH1F('run_'+i,"",10,-4,4)


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

                    HggP4=p1+p2
                    HbbP4=p3+p4
                    m_H1.append(HggP4.M())
                    m_H2.append(HbbP4.M())

                    b_pT.append(p3.Pt())
                    b_eta.append(p3.Eta())
                    b_phi.append(p3.Phi())

                    bbar_pT.append(p4.Pt())
                    bbar_eta.append(p4.Eta())
                    bbar_phi.append(p4.Phi())

                    a_pT.append(p1.Pt())
                    a_eta.append(p1.Eta())
                    a_phi.append(p1.Phi())


    for i in m_H1:
            h_m_H1.Fill(i)
    hists1.append(h_m_H1)

    for i in m_H2:
        h_m_H2.Fill(i)
    hists2.append(h_m_H2)

    for i in b_phi:
            h_b_phi.Fill(i)
    hists3.append(h_b_phi)

    for i in b_eta:
        h_b_eta.Fill(i)
    hists4.append(h_b_eta)

    for i in b_pT:
        h_b_pT.Fill(i)
    hists5.append(h_b_pT)


    for i in bbar_phi:
            h_bbar_phi.Fill(i)
    hists6.append(h_bbar_phi)

    for i in bbar_eta:
        h_bbar_eta.Fill(i)
    hists7.append(h_bbar_eta)

    for i in bbar_pT:
        h_bbar_pT.Fill(i)
    hists8.append(h_bbar_pT)


    for i in a_phi:
            h_a_phi.Fill(i)
    hists9.append(h_a_phi)

    for i in a_eta:
        h_a_eta.Fill(i)
    hists10.append(h_a_eta)

    for i in a_pT:
        h_a_pT.Fill(i)
    hists11.append(h_a_pT)


c=TCanvas("c1","",1500,2000)
#c.SetLogy()
print(len(hists1))

for hist in range(len(hists1)):
    print(hist)
    if hist==0:
        hists1[hist].SetXTitle("M_{#gamma#gamma} [GeV]")
        hists1[hist].SetYTitle("")
        hists1[hist].SetLineColor(hist+1)
        #hists1[hist].SetYRangeUser(0 , .002)
        #hists1[hist].Rebin(5)
        hists1[hist].SetLineWidth(3)
        #hists1[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists1[hist].DrawNormalized('hist')


    else:
        hists1[hist].SetXTitle("M_{#gamma#gamma} [GeV]")
        hists1[hist].SetYTitle("")
        hists1[hist].SetLineColor(hist+1)
        #hists1[hist].Rebin(5)
        hists1[hist].SetLineWidth(3)
        #hists1[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists1[hist].DrawNormalized('hist&same')

#cmsname.Draw()
#legend.Draw()

c.SaveAs("CombinedMassGamma.png")
c.SaveAs("CombinedMassGamma.root")


#############################################################

for hist in range(len(hists2)):
    print(hist)
    if hist==0:
        hists2[hist].SetXTitle("M_{bb~} [GeV]")
        hists2[hist].SetYTitle("")
        hists2[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists2[hist].DrawNormalized('hist')

    else:
        hists2[hist].SetXTitle("M_{bb~} [GeV]")
        hists2[hist].SetYTitle("")
        hists2[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists2[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedMassbb~.png")
c.SaveAs("CombinedMassbb~.root")

#############################################################

for hist in range(len(hists3)):
    print(hist)
    if hist==0:
        hists3[hist].SetXTitle("#phi_(b)")
        hists3[hist].SetYTitle("")
        hists3[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists3[hist].DrawNormalized('hist')

    else:
        hists3[hist].SetXTitle("#phi_(b)")
        hists3[hist].SetYTitle("")
        hists3[hist].SetYTitle("Events")
        hists3[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists3[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedPhi_b.png")
c.SaveAs("CombinedPhi_b.root")

#############################################################

for hist in range(len(hists4)):
    print(hist)
    if hist==0:
        hists4[hist].SetXTitle("#eta_(b)")
        hists4[hist].SetYTitle("")
        hists4[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists4[hist].SetMaximum(500)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists4[hist].DrawNormalized('hist')

    else:
        hists4[hist].SetXTitle("#eta_(b)")
        hists4[hist].SetYTitle("")
        hists4[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists4[hist].SetMaximum(500)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists4[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedEta_b.png")
c.SaveAs("CombinedEta_b.root")

#############################################################

for hist in range(len(hists5)):
    print(hist)
    if hist==0:
        hists5[hist].SetXTitle("p_{T}(b)[GeV]")
        hists5[hist].SetYTitle("")
        hists5[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists5[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists5[hist].DrawNormalized('hist')

    else:
        hists5[hist].SetXTitle("p_{T}(b)[GeV]")
        hists5[hist].SetYTitle("")
        hists5[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists5[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists5[hist].DrawNormalized('hist&same')

c.SaveAs("Combined_pT_b.png")
c.SaveAs("Combined_pT_b.root")

#############################################################

for hist in range(len(hists6)):
    print(hist)
    if hist==0:
        hists6[hist].SetXTitle("#phi_(bbar)")
        hists6[hist].SetYTitle("")
        hists6[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists6[hist].DrawNormalized('hist')

    else:
        hists6[hist].SetXTitle("#phi_(bbar)")
        hists6[hist].SetYTitle("")
        hists6[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists6[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedPhi_bbar.png")
c.SaveAs("CombinedPhi_bbar.root")

#############################################################

for hist in range(len(hists7)):
    print(hist)
    if hist==0:
        hists7[hist].SetXTitle("#eta_(bbar)")
        hists7[hist].SetYTitle("")
        hists7[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists7[hist].SetMaximum(500)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists7[hist].DrawNormalized('hist')

    else:
        hists7[hist].SetXTitle("#eta_(bbar)")
        hists7[hist].SetYTitle("")
        hists7[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists7[hist].SetMaximum(500)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists7[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedEta_bbar.png")
c.SaveAs("CombinedEta_bbar.root")

#############################################################

for hist in range(len(hists8)):
    print(hist)
    if hist==0:
        hists8[hist].SetXTitle("p_{T}(bbar)[GeV]")
        hists8[hist].SetYTitle("")
        hists8[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists8[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists8[hist].DrawNormalized('hist')

    else:
        hists8[hist].SetXTitle("p_{T}(bbar)[GeV]")
        hists8[hist].SetYTitle("")
        hists8[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists8[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists8[hist].DrawNormalized('hist&same')

c.SaveAs("Combined_pT_bbar.png")
c.SaveAs("Combined_pT_bbar.root")

#############################################################

for hist in range(len(hists9)):
    print(hist)
    if hist==0:
        hists9[hist].SetXTitle("#phi_(a)")
        hists9[hist].SetYTitle("")
        hists9[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists9[hist].DrawNormalized('hist')

    else:
        hists9[hist].SetXTitle("#phi_(a)")
        hists9[hist].SetYTitle("")
        hists9[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        #hists[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists9[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedPhi_a.png")
c.SaveAs("CombinedPhi_a.root")

#############################################################

for hist in range(len(hists10)):
    print(hist)
    if hist==0:
        hists10[hist].SetXTitle("#eta_(a)")
        hists10[hist].SetYTitle("")
        hists10[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists10[hist].SetMaximum(500)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists10[hist].DrawNormalized('hist')

    else:
        hists10[hist].SetXTitle("#eta_(a)")
        hists10[hist].SetYTitle("")
        hists10[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists10[hist].SetMaximum(500)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists10[hist].DrawNormalized('hist&same')

c.SaveAs("CombinedEta_a.png")
c.SaveAs("CombinedEta_a.root")

#############################################################

for hist in range(len(hists11)):
    print(hist)
    if hist==0:
        hists11[hist].SetXTitle("p_{T}(a)[GeV]")
        hists11[hist].SetYTitle("")
        hists11[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists11[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists11[hist].DrawNormalized('hist')

    else:
        hists11[hist].SetXTitle("p_{T}(a)[GeV]")
        hists11[hist].SetYTitle("")
        hists11[hist].SetLineColor(hist+1)
        #hists[hist].SetLineWidth(3)
        hists11[hist].SetMaximum(1000)
        #legend.AddEntry(hists[hist],leg_entry[hist],"L")
        hists11[hist].DrawNormalized('hist&same')

c.SaveAs("Combined_pT_a.png")
c.SaveAs("Combined_pT_a.root")
