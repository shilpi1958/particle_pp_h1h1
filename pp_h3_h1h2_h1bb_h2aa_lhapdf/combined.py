import ElementTree2 as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle, TLatex

tree1 = ET.parse('pp_h3_h1h2_h1bb_h2aa_lhapdf.lhe')
root1=tree1.getroot()

eta_b=[]
eta_bbar=[]
phi_b=[]
phi_bbar=[]
phi_a=[]
phi_a2=[]
eta_a=[]
eta_a2=[]
pt_b=[]
pt_a2=[]
pt_bbar=[]
pt_a=[]
m_1_H1=[]
m_1_H2=[]
m_1_H3=[]
m_2_H2=[]
m_2_H1=[]
m_2_H3=[]

m_1_H3=[]
eta_h1=[]
pt_h1=[]
eta_h2=[]
pt_h2=[]
phi_h1=[]
phi_h2=[]


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
       h1=[s for s in lines if s.split()[0]=='25']
       h2=[s for s in lines if s.split()[0]=='35']


       px1=float(h1[0].split()[6])
       py1=float(h1[0].split()[7])
       pz1=float(h1[0].split()[8])
       e1=float(h1[0].split()[9])

       px2=float (h2[0].split()[6])
       py2=float (h2[0].split()[7])
       pz2=float (h2[0].split()[8])
       e2=float (h2[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       ph3 = p1 + p2
       m_1_H3.append(ph3.M())
       eta_h1.append(p1.Eta())
       pt_h1.append(p1.Pt())
       eta_h2.append(p2.Eta())
       pt_h2.append(p2.Pt())
       phi_h1.append(p1.Phi())
       phi_h2.append(p2.Phi())


       px3=float (a1[0].split()[6])
       py3=float (a1[0].split()[7])
       pz3=float (a1[0].split()[8])
       e3=float (a1[0].split()[9])

       px4=float (a2[0].split()[6])
       py4=float (a2[0].split()[7])
       pz4=float (a2[0].split()[8])
       e4=float (a2[0].split()[9])

       p3=TLorentzVector(px3,py3,pz3,e3)
       p4=TLorentzVector(px4,py4,pz4,e4)
       #h2 constructed from  aa
       pb1=p3+p4
       m_1_H2.append(pb1.M())
       eta_a.append(p3.Eta())
       pt_a.append(p3.Pt())
       eta_a2.append(p4.Eta())
       pt_a2.append(p4.Pt())
       phi_a.append(p3.Phi())
       phi_a2.append(p4.Phi())

       px5=float (b1[0].split()[6])
       py5=float (b1[0].split()[7])
       pz5=float (b1[0].split()[8])
       e5=float (b1[0].split()[9])

       px6=float (bbar1[0].split()[6])
       py6=float (bbar1[0].split()[7])
       pz6=float (bbar1[0].split()[8])
       e6=float (bbar1[0].split()[9])

       p5=TLorentzVector(px5,py5,pz5,e5)
       p6=TLorentzVector(px6,py6,pz6,e6)
       #h1 constructed from  bb~
       pb2=p5+p6
       m_1_H1.append(pb2.M())
       eta_b.append(p5.Eta())
       eta_bbar.append(p6.Eta())
       pt_b.append(p5.Pt())
       pt_bbar.append(p6.Pt())
       phi_b.append(p5.Phi())
       phi_bbar.append(p6.Phi())




c.SetLogy()

h1=TH1F('Invariant Mass of H2 (#gamma #gamma)',"",1000,0,1200)
for i in m_1_H2:
        h1.Fill(i)

h14=TH1F('Invariant Mass of H1 (bb~)',"",1000,0,1200)
for i in m_1_H1:
        h14.Fill(i)


h2=TH1F('#eta_{#gamma1}',"",100,-5,5)
for i in eta_a:
        h2.Fill(i)

h9=TH1F('#eta_{#gamma2}',"",100,-5,5)
for i in eta_a2:
        h9.Fill(i)

h3=TH1F('#eta_{b}',"",100,-5,5)
for i in eta_b:
        h3.Fill(i)

h7=TH1F('#eta_{b~}',"",100,-5,5)
for i in eta_bbar:
        h7.Fill(i)

h4=TH1F('P_{t#gamma1}',"",100,0,1000)
for i in pt_a:
        h4.Fill(i)

h8=TH1F('P_{t#gamma2}',"",100,0,1000)
for i in pt_a2:
        h8.Fill(i)

h5=TH1F('Pt of b',"",100,0,1000)
for i in pt_b:
        h5.Fill(i)

h6=TH1F('Pt of bbar',"",100,0,1000)
for i in pt_bbar:
        h6.Fill(i)

h10=TH1F('Phi of a',"",10,-4,4)
for i in phi_a:
        h10.Fill(i)

h11=TH1F('Phi of a2',"",10,-4,5)
for i in phi_a2:
        h11.Fill(i)

h12=TH1F('Phi of b',"",10,-4,4)
for i in phi_b:
        h12.Fill(i)
h13=TH1F('Phi of bbar',"",10,-4,4)
for i in phi_bbar:
        h13.Fill(i)
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

h1.SetXTitle("M_{#gamma#gamma bb~} [GeV]")
h1.SetYTitle("Events")
h1.SetLineColor(6)
#scale1=norm/(h1.Integral())
#h1.Scale(scale1)
#c.SaveAs("Mass_H1.root")
h14.SetXTitle("M_{#gamma#gamma bb~} [GeV]")
h14.SetYTitle("events")
h14.SetLineColor(4)
#scale2=norm/(h14.Integral())
#h14.Scale(scale2)
h1.DrawNormalized("hist")
#c.SaveAs("Mass_H1.png")
h14.DrawNormalized("hist&SAMES")
c.SaveAs("Mass_combine.png")
c.SaveAs("Mass_combine.root")



h2.SetXTitle("#eta_{#gamma}")
h2.SetYTitle("events")
h2.SetLineColor(2)
h9.SetXTitle("#eta_{#gamma}")
h9.SetYTitle("events")
h9.SetLineColor(6)
h2.DrawNormalized("hist")
h9.DrawNormalized("hist&sames")
#legend.Draw()
c.SaveAs("Eta_combine of a.png")
c.SaveAs("Eta_aa_combine.root")

h4.SetXTitle("P_{t#gamma} [GeV]")
h4.SetYTitle("events")
h4.SetLineColor(2)
h8.SetXTitle("P_{t#gamma} [GeV]")
h8.SetYTitle("events")
h4.Draw("hist")
h8.SetLineColor(4)
h8.Draw("hist&sames")
#legend.Draw()
c.SaveAs("Pt_combine_a.png")
c.SaveAs("Pt_combine_a.root")


h10.SetXTitle("#phi_{#gamma2}")
h10.SetYTitle("Events")
h10.SetLineColor(1)
h11.SetXTitle("#phi_{#gamma2}")
h11.SetYTitle("Events")
h11.SetLineColor(3)
#legend.Draw()
h10.Draw()
h11.Draw()
c.SaveAs("Phi_acombined.png")
c.SaveAs("Phi_acombined.root")



h3.SetXTitle("#eta_{b}")
h3.SetYTitle("events")
h3.SetLineColor(2)
h7.SetXTitle("#eta_{b}")
h7.SetYTitle("events")
h7.SetLineColor(4)
h3.Draw("hist")
h7.Draw("hist&sames")
#legend.Draw()
c.SaveAs("Eta of b_combine.png")
c.SaveAs("Eta of b_combine.root")


h5.SetXTitle("Pt of b")
h5.SetYTitle("events")
h5.SetLineColor(2)
h5.Draw()
c.SaveAs("Pt of b.png")

h6.SetXTitle("Pt of bbar")
h6.SetYTitle("events")
h6.SetLineColor(2)
h6.Draw()
c.SaveAs("Pt of bbar.png")

h12.SetXTitle("Phi of b")
h12.SetYTitle("events")
h12.SetLineColor(2)
h12.Draw()
c.SaveAs("Phi of b.png")

h13.SetXTitle("Phi of bbar")
h13.SetYTitle("events")
h13.SetLineColor(2)
h13.Draw()
c.SaveAs("Phi of bbar.png")
