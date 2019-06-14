import ElementTree2 as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle, TLatex

tree1 = ET.parse('pp_h3_h1h2_h1aa_h2bb_lhapdf.lhe')
root1=tree1.getroot()

tree2 = ET.parse('pp_h3_h1h2_h1bb_h2aa_lhapdf.lhe')
root2=tree2.getroot()


eta_b_l1=[]
eta_bbar_l1=[]
phi_b_l1=[]
phi_bbar_l1=[]
phi_a_l1=[]
phi_a2_l1=[]
eta_a_l1=[]
eta_a2_l1=[]
pt_b_l1=[]
pt_a2_l1=[]
pt_bbar_l1=[]
pt_a_l1=[]
m_1_H1_l1=[]
m_1_H2_l1=[]
m_1_H3_l1=[]


eta_b_l2=[]
eta_bbar_l2=[]
phi_b_l2=[]
phi_bbar_l2=[]
phi_a_l2=[]
phi_a2_l2=[]
eta_a_l2=[]
eta_a2_l2=[]
pt_b_l2=[]
pt_a2_l2=[]
pt_bbar_l2=[]
pt_a_l2=[]
m_1_H1_l2=[]
m_1_H2_l2=[]
m_1_H3_l2=[]



gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(1)
gStyle.SetOptStat(111)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
gStyle.SetPadColor(1)

#legend=TLegend(.63,.69,.87,.89,"","#gamma #gamma")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","b b~")

c=TCanvas("c","First canvas",2000,1900)

cmsname=TLatex(0.15,1.85,"Trials")
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)
#lhefdata=LHEFData(float(root.attrib['version']))
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
 if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())

       a1_1=[s for s in lines if s.split()[0]=='22']
       a1=a1_1[1::2]
       a2=a1_1[0::2]
       b1=[s for s in lines if s.split()[0]=='5']
       bbar1=[s for s in lines if s.split()[0]=='-5']

       px3_l1= float (a1[0].split()[6])
       py3_l1= float (a1[0].split()[7])
       pz3_l1= float (a1[0].split()[8])
       e3_l1= float (a1[0].split()[9])

       px4_l1= float (a2[0].split()[6])
       py4_l1= float (a2[0].split()[7])
       pz4_l1= float (a2[0].split()[8])
       e4_l1= float (a2[0].split()[9])

       p3=TLorentzVector(px3_l1,py3_l1,pz3_l1,e3_l1)
       p4=TLorentzVector(px4_l1,py4_l1,pz4_l1,e4_l1)
       #h1 constructed from  aa
       pb1=p3+p4
       m_1_H1_l1.append(pb1.M())
       eta_a_l1.append(p3.Eta())
       pt_a_l1.append(p3.Pt())
       eta_a2_l1.append(p4.Eta())
       pt_a2_l1.append(p4.Pt())
       phi_a_l1.append(p3.Phi())
       phi_a2_l1.append(p4.Phi())

       px5_l1= float (b1[0].split()[6])
       py5_l1= float (b1[0].split()[7])
       pz5_l1= float (b1[0].split()[8])
       e5_l1= float (b1[0].split()[9])

       px6_l1= float (bbar1[0].split()[6])
       py6_l1= float (bbar1[0].split()[7])
       pz6_l1= float (bbar1[0].split()[8])
       e6_l1= float (bbar1[0].split()[9])

       p5=TLorentzVector(px5_l1,py5_l1,pz5_l1,e5_l1)
       p6=TLorentzVector(px6_l1,py6_l1,pz6_l1,e6_l1)
       #h2 constructed from  bb~
       pb2=p5+p6
       m_1_H2_l1.append(pb2.M())
       eta_b_l1.append(p5.Eta())
       eta_bbar_l1.append(p6.Eta())
       pt_b_l1.append(p5.Pt())
       pt_bbar_l1.append(p6.Pt())
       phi_b_l1.append(p5.Phi())
       phi_bbar_l1.append(p6.Phi())

for child in root2:
 if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())

       a1_1=[s for s in lines if s.split()[0]=='22']
       a1=a1_1[1::2]
       a2=a1_1[0::2]
       b1=[s for s in lines if s.split()[0]=='5']
       bbar1=[s for s in lines if s.split()[0]=='-5']

       px3_l2= float (a1[0].split()[6])
       py3_l2= float (a1[0].split()[7])
       pz3_l2= float (a1[0].split()[8])
       e3_l2= float (a1[0].split()[9])

       px4_l2= float (a2[0].split()[6])
       py4_l2= float (a2[0].split()[7])
       pz4_l2= float (a2[0].split()[8])
       e4_l2= float (a2[0].split()[9])

       p3=TLorentzVector(px3_l2,py3_l2,pz3_l2,e3_l2)
       p4=TLorentzVector(px4_l2,py4_l2,pz4_l2,e4_l2)
       #h2 constructed from  aa
       pb1=p3+p4
       m_1_H2_l2.append(pb1.M())
       eta_a_l2.append(p3.Eta())
       pt_a_l2.append(p3.Pt())
       eta_a2_l2.append(p4.Eta())
       pt_a2_l2.append(p4.Pt())
       phi_a_l2.append(p3.Phi())
       phi_a2_l2.append(p4.Phi())

       px5_l2= float (b1[0].split()[6])
       py5_l2= float (b1[0].split()[7])
       pz5_l2= float (b1[0].split()[8])
       e5_l2= float (b1[0].split()[9])

       px6_l2= float (bbar1[0].split()[6])
       py6_l2= float (bbar1[0].split()[7])
       pz6_l2= float (bbar1[0].split()[8])
       e6=float (bbar1[0].split()[9])

       p5=TLorentzVector(px5_l2,py5_l2,pz5_l2,e5_l2)
       p6=TLorentzVector(px6_l2,py6_l2,pz6_l2,e6_l2)
       #h1 constructed from  bb~
       pb2=p5+p6
       m_1_H1_l2.append(pb2.M())
       eta_b_l2.append(p5.Eta())
       eta_bbar_l2.append(p6.Eta())
       pt_b_l2.append(p5.Pt())
       pt_bbar_l2.append(p6.Pt())
       phi_b_l2.append(p5.Phi())
       phi_bbar_l2.append(p6.Phi())



c.SetLogy()

h1_l1=TH1F('Invariant Mass of H1 (#gamma #gamma)',"",1000,0,1200)
for i in m_1_H1_l1:
        h1_l1.Fill(i)

h14_l1=TH1F('Invariant Mass of H2 (bb~)',"",1000,0,1200)
for i in m_1_H2_l1:
        h14_l1.Fill(i)


h2_l1=TH1F('#eta_{#gamma1}',"",100,-5,5)
for i in eta_a_l1:
        h2_l1.Fill(i)

h9_l1=TH1F('#eta_{#gamma2}',"",100,-5,5)
for i in eta_a2_l1:
        h9_l1.Fill(i)

h3_l1=TH1F('#eta_{b}',"",100,-5,5)
for i in eta_b_l1:
        h3_l1.Fill(i)

h7_l1=TH1F('#eta_{b~}',"",100,-5,5)
for i in eta_bbar_l1:
        h7_l1.Fill(i)

h4_l1=TH1F('P_{T#gamma1}',"",100,0,1000)
for i in pt_a_l1:
        h4_l1.Fill(i)

h8_l1=TH1F('P_{T#gamma2}',"",100,0,1000)
for i in pt_a2_l1:
        h8_l1.Fill(i)

h5_l1=TH1F('Pt of b',"",100,0,1000)
for i in pt_b_l1:
        h5_l1.Fill(i)

h6_l1=TH1F('Pt of bbar',"",100,0,1000)
for i in pt_bbar_l1:
        h6_l1.Fill(i)

h10_l1=TH1F('Phi of a',"",10,-4,4)
for i in phi_a_l1:
        h10_l1.Fill(i)

h11_l1=TH1F('Phi of a2',"",10,-4,5)
for i in phi_a2_l1:
        h11_l1.Fill(i)

h12_l1=TH1F('Phi of b',"",10,-4,4)
for i in phi_b_l1:
        h12_l1.Fill(i)
h13_l1=TH1F('Phi of bbar',"",10,-4,4)
for i in phi_bbar_l1:
        h13_l1.Fill(i)




h1_l2=TH1F('Invariant Mass of H1 (bb~)',"",1000,0,1200)
for i in m_1_H1_l2:
        h1_l2.Fill(i)

h14_l2=TH1F('Invariant Mass of H2 (#gamma #gamma)',"",1000,0,1200)
for i in m_1_H2_l2:
        h14_l2.Fill(i)


h2_l2=TH1F('#eta_{#gamma1}',"",100,-5,5)
for i in eta_a_l2:
        h2_l2.Fill(i)

h9_l2=TH1F('#eta_{#gamma2}',"",100,-5,5)
for i in eta_a2_l2:
        h9_l2.Fill(i)

h3_l2=TH1F('#eta_{b}',"",100,-5,5)
for i in eta_b_l2:
        h3_l2.Fill(i)

h7_l2=TH1F('#eta_{b~}',"",100,-5,5)
for i in eta_bbar_l2:
        h7_l2.Fill(i)

h4_l2=TH1F('P_{T#gamma1}',"",100,0,1000)
for i in pt_a_l2:
        h4_l2.Fill(i)

h8_l2=TH1F('P_{T#gamma2}',"",100,0,1000)
for i in pt_a2_l2:
        h8_l2.Fill(i)

h5_l2=TH1F('Pt of b',"",100,0,1000)
for i in pt_b_l2:
        h5_l2.Fill(i)

h6_l2=TH1F('Pt of bbar',"",100,0,1000)
for i in pt_bbar_l2:
        h6_l2.Fill(i)

h10_l2=TH1F('Phi of a',"",10,-4,4)
for i in phi_a_l2:
        h10_l2.Fill(i)

#h11_l2=TH1F('Phi of a2',"",10,-4,5)
#for i in phi_a2_l2:
#        h11_l2.Fill(i)

h12_l2=TH1F('Phi of b',"",10,-4,4)
for i in phi_b_l2:
        h12_l2.Fill(i)
h13_l2=TH1F('Phi of bbar',"",10,-4,4)
for i in phi_bbar_l2:
        h13_l2.Fill(i)



'''
tps1=TPaveStats()
h1.FindObject("stats")
tps1.SetName("Hist1 Stats")
X1=tps1.GetX1NDC()
Y1=tps1.GetY1NDC()
X2=tps1.GetX2NDC()
Y2=tps1.GetY2NDC()

tps2=TPaveStats()
h14.FindObject("stats")
tps2.SetTextColor(kRed)
tps2.SetLineColor(kRed)
tps2.SetX1NDC(X1)
tps2.SetX2NDC(X2)
tps2.SetY1NDC(Y1-(Y2-Y1))
tps2.SetY2NDC(Y1)
'''
'''
legend=TLegend(0.1,0.1,0.3,0.3)
legend.SetHeader("Legend")
legend.AddEntry(h2,"#eta_{#gamma1}","l")
legend.AddEntry(h9,"#eta_{#gamma2}","l")
legend.AddEntry(h3,"#eta_{b}","l")
legend.AddEntry(h7,"#eta_{b~}","l")
legend.AddEntry(h4,"pt_{#gamma1}","l")
legend.AddEntry(h8,"pt_{#gamma2}","l")
legend.AddEntry(h4,"pt_{#gamma1}","l")
legend.AddEntry(h8,"pt_{#gamma2}","l")
'''

h1_l1.SetXTitle("M_h1_aa [GeV]")
h1_l1.SetYTitle("Events")
h1_l1.SetLineColor(6)
h1_l2.SetXTitle("M_h1_bb [GeV]")
h1_l2.SetYTitle("events")
h1_l2.SetLineColor(4)
h1_l1.DrawNormalized("hist")
h1_l2.DrawNormalized("hist&SAMES")
c.SaveAs("Mass_combine_h1.png")
c.SaveAs("Mass_combine_h1.root")

h14_l1.SetXTitle("M_h2_bb [GeV]")
h14_l1.SetYTitle("Events")
h14_l1.SetLineColor(6)
h14_l2.SetXTitle("M_h1_aa [GeV]")
h14_l2.SetYTitle("events")
h14_l2.SetLineColor(4)
h14_l1.DrawNormalized("hist")
h14_l2.DrawNormalized("hist&SAMES")
c.SaveAs("Mass_combine_h2.png")
c.SaveAs("Mass_combine_h2.root")

h2_l1.SetXTitle("#eta_{#gamma}")
h2_l1.SetYTitle("Events")
h2_l1.SetLineColor(6)
h2_l2.SetXTitle("#eta_{#gamma}")
h2_l2.SetYTitle("events")
h2_l2.SetLineColor(4)
h2_l1.DrawNormalized("hist")
h2_l2.DrawNormalized("hist&SAMES")
c.SaveAs("eta_combine_gamma.png")
c.SaveAs("eta_combine_gamma.root")

h3_l1.SetXTitle("#eta_{b}")
h3_l1.SetYTitle("Events")
h3_l1.SetLineColor(6)
h3_l2.SetXTitle("#eta_{b}")
h3_l2.SetYTitle("events")
h3_l2.SetLineColor(4)
h3_l1.DrawNormalized("hist")
h3_l2.DrawNormalized("hist&SAMES")
c.SaveAs("eta_combine_b.png")
c.SaveAs("eta_combine_b.root")

h4_l1.SetXTitle("p_{T#gamma} ")
h4_l1.SetYTitle("Events")
h4_l1.SetLineColor(6)
h4_l2.SetXTitle("p_{T#gamma}")
h4_l2.SetYTitle("events")
h4_l2.SetLineColor(4)
h4_l1.DrawNormalized("hist")
h4_l2.DrawNormalized("hist&SAMES")
c.SaveAs("pT_combine_gamma.png")
c.SaveAs("pT_combine_gamma.root")

h5_l1.SetXTitle("#p_{T}_b")
h5_l1.SetYTitle("Events")
h5_l1.SetLineColor(6)
h5_l2.SetXTitle("#p_{T}_b")
h5_l2.SetYTitle("events")
h5_l2.SetLineColor(4)
h5_l1.DrawNormalized("hist")
h5_l2.DrawNormalized("hist&SAMES")
c.SaveAs("pT_combine_b.png")
c.SaveAs("pT_combine_b.root")

h6_l1.SetXTitle("#p_{T}_b~")
h6_l1.SetYTitle("Events")
h6_l1.SetLineColor(6)
h6_l2.SetXTitle("#p_{T}_b~")
h6_l2.SetYTitle("events")
h6_l2.SetLineColor(4)
h6_l1.DrawNormalized("hist")
h6_l2.DrawNormalized("hist&SAMES")
c.SaveAs("pT_combine_b~.png")
c.SaveAs("pT_combine_b~.root")

h7_l1.SetXTitle("#eta_{b~}")
h7_l1.SetYTitle("Events")
h7_l1.SetLineColor(6)
h7_l2.SetXTitle("#eta_{b~}")
h7_l2.SetYTitle("events")
h7_l2.SetLineColor(4)
h7_l1.DrawNormalized("hist")
h7_l2.DrawNormalized("hist&SAMES")
c.SaveAs("eta_combine_b~.png")
c.SaveAs("eta_combine_b~.root")

h10_l1.SetXTitle("#phi_{#gamma2}")
h10_l1.SetYTitle("Events")
h10_l1.SetLineColor(6)
h10_l2.SetXTitle("#phi_{#gamma2}")
h10_l2.SetYTitle("events")
h10_l2.SetLineColor(4)
h10_l1.DrawNormalized("hist")
h10_l2.DrawNormalized("hist&SAMES")
c.SaveAs("phi_combine_gamma.png")
c.SaveAs("phi_combine_gamma.root")

h12_l1.SetXTitle("#phi_{b}")
h12_l1.SetYTitle("Events")
h12_l1.SetLineColor(6)
h12_l2.SetXTitle("#phi_{b}")
h12_l2.SetYTitle("events")
h12_l2.SetLineColor(4)
h12_l1.DrawNormalized("hist")
h12_l2.DrawNormalized("hist&SAMES")
c.SaveAs("phi_combine_b.png")
c.SaveAs("phi_combine_b.root")

h13_l1.SetXTitle("#phi_{b~}")
h13_l1.SetYTitle("Events")
h13_l1.SetLineColor(6)
h13_l2.SetXTitle("#phi_{b~}")
h13_l2.SetYTitle("events")
h13_l2.SetLineColor(4)
h13_l1.DrawNormalized("hist")
h13_l2.DrawNormalized("hist&SAMES")
c.SaveAs("phi_combine_b~.png")
c.SaveAs("phi_combine_b~.root")
