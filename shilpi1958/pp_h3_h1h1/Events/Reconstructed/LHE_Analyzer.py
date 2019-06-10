import ElementTree as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle,TLatex


tree1 = ET.parse('pp_h3_h1h1.lhe')
root1=tree1.getroot()
pt_phi1=[]
pt_b=[]
pt_bbar=[]
eta_b=[]
eta_bbar=[]
met=[]
DR=[]
m_H=[]
phi_b=[]
phi_bbar=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","brNDC")
c = TCanvas()

cmsname=TLatex(0.15,0.95,'Trials')
#cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)
#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())
    
       '''
phi=[s for s in lines if s.split()[0]=='5'] 
       chi=[s for s in lines if s.split()[0]=='52']
       chibar=[s for s in lines if s.split()[0]=='-52']
       '''
              
       b_1=[s for s in lines if s.split()[0]=='25']
       b = b_1[1::2]
       bbar=b_1[0::2]
       
          
       '''
       if phi:
           
           px=float (phi[0].split()[6])
           py=float (phi[0].split()[7])
           pz=float (phi[0].split()[8])
           e=float (phi[0].split()[9])
           p=TLorentzVector(px,py,pz,e)          
           pt_phi1.append(p.Pt())

       
       px1=float (chi[0].split()[6])
       py1=float (chi[0].split()[7])
       pz1=float (chi[0].split()[8])
       e1=float (chi[0].split()[9])

       px2=float (chibar[0].split()[6])
       py2=float (chibar[0].split()[7])
       pz2=float (chibar[0].split()[8])
       e2=float (chibar[0].split()[9])

       p1=TLorentzVector(px1,py1,pz1,e1)
       p2=TLorentzVector(px2,py2,pz2,e2)

       pi=p1+p2
      
       met.append(pi.Pt())
'''       
       px3=float (b[0].split()[6])
       py3=float (b[0].split()[7])
       pz3=float (b[0].split()[8])
       e3=float (b[0].split()[9])
       
       px4=float (bbar[0].split()[6])
       py4=float (bbar[0].split()[7])
       pz4=float (bbar[0].split()[8])
       e4=float (bbar[0].split()[9])

       p3=TLorentzVector(px3,py3,pz3,e3)
       p4=TLorentzVector(px4,py4,pz4,e4)
       pb=p3+p4
       pt_b.append(p3.Pt())
       eta_b.append(p3.Eta())
       m_H.append(pb.M())
       phi_b.append(p3.Phi())
       pt_bbar.append(p4.Pt())
       eta_bbar.append(p4.Eta())
       DR.append(abs(p3.DeltaR(p4)))
       phi_bbar.append(p4.Phi())
'''
h1_met=TH1F("genMET","",100,0,1000)
for i in met:
        h1_met.Fill(i)
'''        
h1_DR=TH1F("DR(b,bbar)","",5,0,5)
for i in DR:
        h1_DR.Fill(i)

h_ptb=TH1F("pT of h3 ","",100,0,500)
for i in pt_b:
        h_ptb.Fill(i)

h_etab=TH1F("Eta of h3 ","",10,-5,5)
for i in eta_b:
        h_etab.Fill(i)

h_ptbbar=TH1F("pT of h3 ","",100,0,1000)
for i in pt_bbar:
       h_ptbbar.Fill(i)

h_etabbar=TH1F("Eta of h3 ","",10,-5,5)
for i in eta_bbar:
       h_etabbar.Fill(i)

h1_m_H=TH1F("Mass of h3","",100,200,800)
for i in m_H:
        h1_m_H.Fill(i)

h_phi_b=TH1F("Phi of h3 ","",10,-5,5)
for i in phi_b:
        h_phi_b.Fill(i)

h_phi_bbar=TH1F("Phi of h3 ","",10,-5,5)
for i in phi_bbar:
        h_phi_bbar.Fill(i)


c=TCanvas()
'''
c.SetLogy()
'''
'''
h1_met.SetXTitle("genMET[GeV]")
h1_met.SetYTitle("Events")
h1_met.Draw()
cmsname.Draw()
c.SaveAs("met.pdf")
'''
'''
h1_DR.SetXTitle("#DeltaR(b,bbar)")
h1_DR.SetYTitle("Events")
h1_DR.Draw()
cmsname.Draw()
c.SaveAs("DR.png")
'''
h_ptb.SetXTitle("pT of h3 ")
h_ptb.SetYTitle("Events")
h_ptb.Draw()
cmsname.Draw()
c.SaveAs("pt_h3_reconstructed.png")

h_etab.SetXTitle("Eta of h3 ")
h_etab.SetYTitle("Events")
h_etab.Draw()
cmsname.Draw()
c.SaveAs("eta_h3_reconstructed.png")
'''
h_ptbbar.SetXTitle("pT of h1 ")
h_ptbbar.SetYTitle("Events")
h_ptbbar.Draw()
cmsname.Draw()
c.SaveAs("ptbbar.png")

h_etabbar.SetXTitle("Eta of h3 ")
h_etabbar.SetYTitle("Events")
h_etabbar.Draw()
cmsname.Draw()
c.SaveAs("etabbar.png")
'''
h1_m_H.SetXTitle("Mass of h3")
h1_m_H.SetYTitle("Events")
h1_m_H.Draw()
cmsname.Draw()
c.SaveAs("mass_h3_reconstructed.png")

h_phi_b.SetXTitle("Phi of h3 ")
h_phi_b.SetYTitle("Phi of h3 ")
h_phi_b.Draw()
cmsname.Draw()
c.SaveAs("Phi_h3_reconstructed .png")
'''
h_phi_bbar.SetXTitle("Phi of h1 ")
h_phi_bbar.SetYTitle("Phi of h1 ")
h_phi_bbar.Draw()
cmsname.Draw()
c.SaveAs("Phi_h1_reconstructed.png")
'''
#c.BuildLegend(0.3,0.7,0.58,0.9,"(M_{#chi}=1, M_{#phi}=1000)")


