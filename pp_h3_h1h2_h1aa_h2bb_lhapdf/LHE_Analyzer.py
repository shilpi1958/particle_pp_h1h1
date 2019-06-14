
import ElementTree2 as ET
from ROOT import TLorentzVector, TCanvas, TH1F, TLegend, gStyle, TLatex

tree1 = ET.parse('pp_h2_h1h1_bbaa.lhe')
root1 = tree1.getroot()
phi_bbar = []
phi_b = []
pt_b = []
pt_bbar = []
eta_b = []
eta_bbar = []
e_b = []
e_bbar = []
met = []
DR = []
m_h = []
phi_h = []
eta_h = []
pt_h = []

phi_phobar = []
phi_pho = []
pt_pho = []
pt_phobar = []
eta_pho = []
eta_phobar = []
e_pho = []
e_phobar = []
DR_pho = []
m_h_pho = []
phi_h_pho = []
eta_h_pho = []
pt_h_pho = []

p3 = []
p4 = []

gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(1)
# gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(2)
gStyle.SetLineWidth(1)
# gStyle.SetPadColor(1)
# legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","brNDC")
c = TCanvas()

cmsname = TLatex(0.15, 0.95, '  ')
# cmsname=TLatex(0.15,1.85,"CMS #it{#bf{Preliminary}}")
cmsname.SetTextSize(0.036)
cmsname.SetTextAlign(12)
cmsname.SetNDC(1)
cmsname.SetTextFont(61)
# lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag == 'event'):
        lines = child.text.strip().split('\n')
        event_header = lines[0].strip()
        num_part = int(event_header.split()[0].strip())

        photon = [s for s in lines if s.split()[0] == '22']
        pho = photon[1::2]
        phobar = photon[0::2]
        phi = [s for s in lines if s.split()[0] == '5' and ((s.split()[2] == '5' and lines[3].split()[0] == '25') or (s.split()[2] == '4' and lines[4].split()[0] == '25'))]
        chi = [s for s in lines if s.split()[0] == '-5' and ((s.split()[2] == '5' and lines[3].split()[0] == '25') or (s.split()[2] == '4' and lines[4].split()[0] == '25'))]

        p = []
        p1 = []
        if phi:
            px = float(phi[0].split()[6])
            py = float(phi[0].split()[7])
            pz = float(phi[0].split()[8])
            e = float(phi[0].split()[9])
            m = float(phi[0].split()[10])
            p = TLorentzVector(px, py, pz, e)
            pt_b.append(p.Pt())
            eta_b.append(p.Eta())
            e_b.append(p.E())
            phi_b.append(p.Phi())

        if pho:
            px3 = float(pho[0].split()[6])
            py3 = float(pho[0].split()[7])
            pz3 = float(pho[0].split()[8])
            e3 = float(pho[0].split()[9])
            p3 = TLorentzVector(px3, py3, pz3, e3)
            pt_pho.append(p3.Pt())
            eta_pho.append(p3.Eta())
            e_pho.append(p3.E())
            phi_pho.append(p3.Phi())

        if phobar:
            px4 = float(phobar[0].split()[6])
            py4 = float(phobar[0].split()[7])
            pz4 = float(phobar[0].split()[8])
            e4 = float(phobar[0].split()[9])
            p4 = TLorentzVector(px4, py4, pz4, e4)
            pt_phobar.append(p4.Pt())
            eta_phobar.append(p4.Eta())
            e_phobar.append(p4.E())
            phi_phobar.append(p4.Phi())

        if chi:
            px1 = float(chi[0].split()[6])
            py1 = float(chi[0].split()[7])
            pz1 = float(chi[0].split()[8])
            e1 = float(chi[0].split()[9])
            p1 = TLorentzVector(px1, py1, pz1, e1)
            pt_bbar.append(p1.Pt())
            eta_bbar.append(p1.Eta())
            e_bbar.append(p1.E())
            phi_bbar.append(p1.Phi())

        if chi and phi:
            pi = []
            pi = p+p1
            m_h.append(pi.M())
            DR.append(abs(p.DeltaR(p1)))
            phi_h.append(pi.Phi())
            eta_h.append(pi.Eta())
            pt_h.append(pi.Pt())

        if pho and phobar:
            pb = []
            pb = p3+p4
            m_h_pho.append(pb.M())
            DR_pho.append(abs(p3.DeltaR(p4)))
            phi_h_pho.append(pb.Phi())
            eta_h_pho.append(pb.Eta())
            pt_h_pho.append(pb.Pt())


'''
px2=float (chibar[0].split()[6])
py2=float (chibar[0].split()[7])
pz2=float (chibar[0].split()[8])
e2=float (chibar[0].split()[9])

p1=TLorentzVector(px1,py1,pz1,e1)
p2=TLorentzVector(px2,py2,pz2,e2)

pi=p1+p2

met.append(pi.Pt())

h1_met=TH1F("genMET","",100,0,1000)
for i in met:
    h1_met.Fill(i)

'''

h_mass = TH1F("Mass_of_h", "", 3000, 120, 130)
for i in m_h:
    h_mass.Fill(i)


h_phi_h = TH1F("Phi_of_h", "", 10, -5, 5)
for i in phi_h:
    h_phi_h.Fill(i)

h_eta_h = TH1F("Eta_of_h", "", 10, -8, 8)
for i in eta_b:
    h_eta_h.Fill(i)

h_pt_h = TH1F("pT_of_h", "", 100, -10, 500)
for i in pt_h:
    h_pt_h.Fill(i)

h1_DR = TH1F("DR(b,bbar)", "", 50, -2, 8)
for i in DR:
    h1_DR.Fill(i)

h_eb = TH1F("Energy_of_b", "", 100, -100, 2000)
for i in e_b:
    h_eb.Fill(i)

h_ptb = TH1F("pT_of_b", "", 100, -10, 500)
for i in pt_b:
    h_ptb.Fill(i)

h_etab = TH1F("Eta_of_b", "", 10, -8, 8)
for i in eta_b:
    h_etab.Fill(i)

h_phib = TH1F("Phi_of_b", "", 10, -5, 5)
for i in phi_b:
    h_phib.Fill(i)

h_ebbar = TH1F("Energy_of_bbar", "", 100, -100, 2000)
for i in e_bbar:
    h_ebbar.Fill(i)

h_ptbbar = TH1F("pT_of_bbar", "", 100, -10, 500)
for i in pt_bbar:
    h_ptbbar.Fill(i)

h_etabbar = TH1F("Eta_of_bbar", "", 10, -8, 8)
for i in eta_bbar:
    h_etabbar.Fill(i)

h_phibbar = TH1F("Phi_of_bbar", "", 10, -5, 5)
for i in phi_bbar:
    h_phibbar.Fill(i)


h_mass_pho = TH1F("Mass_of_h", "", 3000, 120, 130)
for i in m_h_pho:
    h_mass_pho.Fill(i)

h_phi_pho = TH1F("Phi_of_h", "", 10, -5, 5)
for i in phi_h_pho:
    h_phi_pho.Fill(i)

h_eta_pho = TH1F("Eta_of_h", "", 10, -8, 8)
for i in eta_pho:
    h_eta_pho.Fill(i)

h_pt_pho = TH1F("pT_of_h", "", 100, -10, 500)
for i in pt_h_pho:
    h_pt_pho.Fill(i)

h1_DR_pho = TH1F("DR(pho,pho)", "", 50, -2, 8)
for i in DR_pho:
    h1_DR_pho.Fill(i)

h_e_pho = TH1F("Energy_of_b", "", 100, -100, 2000)
for i in e_pho:
    h_e_pho.Fill(i)

h_pt_pho = TH1F("pT_of_b", "", 100, -10, 500)
for i in pt_pho:
    h_pt_pho.Fill(i)

h_eta_pho = TH1F("Eta_of_b", "", 10, -8, 8)
for i in eta_pho:
    h_eta_pho.Fill(i)

h_phi_pho = TH1F("Phi_of_b", "", 10, -5, 5)
for i in phi_pho:
    h_phi_pho.Fill(i)


# c=TCanvas()
# c.SetLogy()

'''
h1_met.SetXTitle("genMET[GeV]")
h1_met.SetYTitle("Events")
h1_met.Draw()
cmsname.Draw()
c.SaveAs("met.pdf")
'''
'''

h_mass.SetXTitle("Mass_of_h1[GeV] normalized")
h_mass.SetYTitle("Events")
#h_mass_area = 1/(h_mass.Integral())
#h_mass.Scale(h_mass_area)
cmsname.SetLineColor(3)

#h_mass_pho.SetXTitle("Mass_of_h1_pho[GeV] normalized")
#h_mass_pho.SetYTitle("Events")
#h_mass_pho_area = 1/(h_mass_pho.Integral())
#h_mass.Scale(h_mass_pho_area)
#cmsname.SetLineColor(4)

cmsname.Draw()
h_mass.Draw()
#h_mass_pho.Draw("same")
c.SaveAs("mass_of_h1_combine.root")


'''
h_mass.SetXTitle("Mass_of_h1[GeV] from b")
h_mass.SetYTitle("Events")
h_mass.Draw()
cmsname.Draw()
c.SaveAs("mass_of_h1 from b .root")

h_phi_h.SetXTitle("Phi_of_h1 from b")
h_phi_h.SetYTitle("Events")
h_phi_h.Draw()
cmsname.Draw()
c.SaveAs("phi_of_h1 from b.root")

h_eta_h.SetXTitle("Eta_of_h11 from b")
h_eta_h.SetYTitle("Events")
h_eta_h.Draw()
cmsname.Draw()
c.SaveAs("eta_of_h1 from b .root")

h_pt_h.SetXTitle("Pt_of_h1 from b")
h_pt_h.SetYTitle("Events")
h_pt_h.Draw()
cmsname.Draw()
c.SaveAs("pt_of_h1 from b.root")

h1_DR.SetXTitle("#DeltaR(b,bbar)")
h1_DR.SetYTitle("Events")
h1_DR.Draw()
cmsname.Draw()
c.SaveAs("DR for h1.root")

h_eb.SetXTitle("Energy_of_b from h1")
h_eb.SetYTitle("Events")
h_eb.Draw()
cmsname.Draw()
c.SaveAs("eb_of_h1.root")

h_ptb.SetXTitle("pT_of_b from h1")
h_ptb.SetYTitle("Events")
h_ptb.Draw()
cmsname.Draw()
c.SaveAs("ptb_of_h1.root")

h_etab.SetXTitle("Eta_of_b from h1")
h_etab.SetYTitle("Events")
h_etab.Draw()
cmsname.Draw()
c.SaveAs("etab_of_h1.root")

h_phib.SetXTitle("Phi_of_b from h1")
h_phib.SetYTitle("Events")
h_phib.Draw()
cmsname.Draw()
c.SaveAs("Phib_of_h1.root")

h_ebbar.SetXTitle("Energy_of_b~ from h1")
h_ebbar.SetYTitle("Events")
h_ebbar.Draw()
cmsname.Draw()
c.SaveAs("ebbar_of_h1.root")

h_ptbbar.SetXTitle("pT_of_b~ from h1")
h_ptbbar.SetYTitle("Events")
h_ptbbar.Draw()
cmsname.Draw()
c.SaveAs("ptbbar_of_h1.root")

h_etabbar.SetXTitle("Eta_of_b~ h1")
h_etabbar.SetYTitle("Events")
h_etabbar.Draw()
cmsname.Draw()
c.SaveAs("etabbar_of_h1.root")

h_phibbar.SetXTitle("Phi_of_b~ from h1")
h_phibbar.SetYTitle("Events")
h_phibbar.Draw()
cmsname.Draw()
c.SaveAs("Phibbar_of_h1.root")

h_mass_pho.SetXTitle("Mass_of_h1_pho[GeV]")
h_mass_pho.SetYTitle("Events")
h_mass_pho.Draw()
cmsname.Draw()
c.SaveAs("mass_of_h_pho.root")

h_phi_pho.SetXTitle("Phi_of_h1_pho")
h_phi_pho.SetYTitle("Events")
h_phi_pho.Draw()
cmsname.Draw()
c.SaveAs("phi_of_h_pho.root")

h_eta_pho.SetXTitle("Eta_of_h1_pho")
h_eta_pho.SetYTitle("Events")
h_eta_pho.Draw()
cmsname.Draw()
c.SaveAs("eta_of_h1_pho.root")

h_pt_pho.SetXTitle("Pt_of_h1_pho")
h_pt_pho.SetYTitle("Events")
h_pt_pho.Draw()
cmsname.Draw()
c.SaveAs("pt_of_h_pho.root")

h1_DR_pho.SetXTitle("#DeltaR(pho,pho)")
h1_DR_pho.SetYTitle("Events")
h1_DR_pho.Draw()
cmsname.Draw()
c.SaveAs("DR for h_pho.root")

h_e_pho.SetXTitle("Energy_of_pho from h")
h_e_pho.SetYTitle("Events")
h_e_pho.Draw()
cmsname.Draw()
c.SaveAs("e_of_pho.root")

h_pt_pho.SetXTitle("pT_of_pho from h")
h_pt_pho.SetYTitle("Events")
h_pt_pho.Draw()
cmsname.Draw()
c.SaveAs("ptb_of_pho.root")

h_eta_pho.SetXTitle("Eta_of_pho from h")
h_eta_pho.SetYTitle("Events")
h_eta_pho.Draw()
cmsname.Draw()
c.SaveAs("etab_of_pho.root")

h_phi_pho.SetXTitle("Phi_of_pho from h")
h_phi_pho.SetYTitle("Events")
h_phi_pho.Draw()
cmsname.Draw()
c.SaveAs("Phib_of_pho.root")


# c.BuildLegend(0.3,0.7,0.58,0.9,"(M_{#chi}=1, M_{#phi}=1000)")
