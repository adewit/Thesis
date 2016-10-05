#!/usr/bin/env python
import ROOT
from array import array
import CombineHarvester.CombineTools.plotting as plot
import numpy as np

def set_plot_style():
  NRGBs = 5;
  NCont = 255;
  stops = {0.00,0.34,0.61,0.84,1.00}
  red = {0.00,0.00,0.87,1.00,0.51}
  green = {0.00,0.81,1.00,0.20,0.00} 
  blue = {0.51,1.00,0.12,0.00,0.00}
  ROOT.TColor.CreateGradientColorTable(NRGBs,np.array(stops),np.array(red),np.array(green),np.array(blue),NCont)
  ROOT.gStyle.SetNumberContours(NCont)

def DrawAxisHists(pads, axis_hists, def_pad=None):
    for i, pad in enumerate(pads):
        pad.cd()
        axis_hists[i].Draw('AXIS')
        axis_hists[i].Draw('AXIGSAME')
    if def_pad is not None:
        def_pad.cd()




#plot.ModTDRStyle(r=0.17, l=0.12)
#ROOT.gStyle.SetNdivisions(510, 'XYZ')
set_plot_style()
#plot.SetBirdPalette()

ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetCanvasColor(ROOT.kWhite)
ROOT.gStyle.SetCanvasDefH(600)  # Height of canvas
ROOT.gStyle.SetCanvasDefW(600)  # Width of canvas
ROOT.gStyle.SetCanvasDefX(0)    # POsition on screen
ROOT.gStyle.SetCanvasDefY(0)

ROOT.gStyle.SetPadBorderMode(0)
# ROOT.gStyle.SetPadBorderSize(Width_t size = 1)
ROOT.gStyle.SetPadColor(ROOT.kWhite)
ROOT.gStyle.SetPadGridX(False)
ROOT.gStyle.SetPadGridY(False)
ROOT.gStyle.SetGridColor(0)
ROOT.gStyle.SetGridStyle(3)
ROOT.gStyle.SetGridWidth(1)

# For the frame:
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetFrameBorderSize(1)
ROOT.gStyle.SetFrameFillColor(0)
ROOT.gStyle.SetFrameFillStyle(0)
ROOT.gStyle.SetFrameLineColor(1)
ROOT.gStyle.SetFrameLineStyle(1)
ROOT.gStyle.SetFrameLineWidth(1)

ROOT.gStyle.SetPadLeftMargin(0.12)
# default 0.16
ROOT.gStyle.SetPadRightMargin(0.17)





f1 = ROOT.TFile("../../../auxiliaries/models/2HDM_ty2_mA300_mH300.root")
f2 = ROOT.TFile("cmb_2HDMtyp2-cosba-tanb-hhh.root")
f3 = ROOT.TFile("cmb_2HDMtyp2-cosba-tanb-azh.root")

tree = f1.Get("Tree2HDM");

hhexp0 = f2.Get("cmb/gr_expected_0")
hhexp1 = f2.Get("cmb/gr_expected_1")
hhexp2 = f2.Get("cmb/gr_expected_2")
hhexp3 = f2.Get("cmb/gr_expected_3")
hhobs0 = f2.Get("cmb/gr_observed_0")
hhobs1 = f2.Get("cmb/gr_observed_1")
hhobs2 = f2.Get("cmb/gr_observed_2")
hhobs3 = f2.Get("cmb/gr_observed_3")

exparr = {hhexp0,hhexp1,hhexp2,hhexp3}
obsarr = {hhobs0,hhobs1,hhobs2,hhobs3}

zhexp0 = f3.Get("cmb/gr_expected_0")
zhexp1 = f3.Get("cmb/gr_expected_1")
zhexp2 = f3.Get("cmb/gr_expected_2")
zhobs0 = f3.Get("cmb/gr_observed_0")
zhobs1 = f3.Get("cmb/gr_observed_1")
zhobs2 = f3.Get("cmb/gr_observed_2")



tanb = array('f',[0.])
cosba = array('f',[0.])
xsH = array('f',[0.])
xsA =array('f',[0.])
brH =array('f',[0.])
brA =array('f',[0.])
brhtautau=array('f',[0.])
brhbb=array('f',[0.])

tree.SetBranchAddress("tanbeta",tanb)
tree.SetBranchAddress("cosba",cosba)
tree.SetBranchAddress("ggH",xsH)
tree.SetBranchAddress("ggA",xsA)
BrH = tree.GetLeaf("BRH","hh")
BrA = tree.GetLeaf("BRA","Zh")
Brhtt = tree.GetLeaf("BRh","tautau")
BRhbb = tree.GetLeaf("BRh","bb")
BrH.SetAddress(brH)
BrA.SetAddress(brA)
Brhtt.SetAddress(brhtautau)
BRhbb.SetAddress(brhbb)

ybins = np.array([0.025,0.075,0.125,0.175,0.225,0.275,0.325,0.375,0.425,0.475,0.525,0.575,0.625,0.675,0.725,0.775,0.825,0.875,0.925,0.975,1.025,1.075,1.125,1.175,1.225,1.275,1.325,1.375,1.425,1.475,1.525,1.575,1.625,1.675,1.725,1.775,1.825,1.875,1.925,1.975,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.25,3.75,4.25,4.75,5.25,5.75,6.25,6.75,7.25,7.75,8.25,8.75,9.25,9.75,10])
XSTimesBR_A = ROOT.TH2F("XSTimesBR_A","XSTimesBR_A",101,-1.01,1.01,64, ybins)
XSTimesBR_H = ROOT.TH2F("XSTimesBR_H","XSTimesBR_H",101,-1.01,1.01,64, ybins)
h_top = ROOT.TH2F("htop","htop",101,-1.01,1.01,64, ybins)
h_top.SetTitle("")
h_top.SetStats(0)


nVals = tree.GetEntries();
tree.Print()
for i in range(0,nVals):
  tree.GetEntry(i);
  globalbin = XSTimesBR_A.FindBin(cosba[0],tanb[0])
  contents = XSTimesBR_A.GetBinContent(globalbin)
  if(contents==0):
    print cosba[0]
    print tanb[0]
    print xsA[0]
    XSTimesBR_A.Fill(cosba[0],tanb[0],xsA[0]*brA[0]*brhtautau[0]*0.10099)
    XSTimesBR_H.Fill(cosba[0],tanb[0],xsH[0]*brH[0]*brhtautau[0]*brhbb[0]*2)


zhexp0.SetLineColor(ROOT.kBlue+3);
zhexp1.SetLineColor(ROOT.kBlue+3);
zhexp2.SetLineColor(ROOT.kBlue+3);
zhexp0.SetLineStyle(2);
zhexp1.SetLineStyle(2);
zhexp2.SetLineStyle(2);
zhobs0.SetLineColor(ROOT.kBlue+3);
zhobs1.SetLineColor(ROOT.kBlue+3);
zhobs2.SetLineColor(ROOT.kBlue+3);
zhobs0.SetLineStyle(1);
zhobs1.SetLineStyle(1);
zhobs2.SetLineStyle(1);


hhexp0.SetLineColor(ROOT.kBlue+3);
hhexp1.SetLineColor(ROOT.kBlue+3);
hhexp2.SetLineColor(ROOT.kBlue+3);
hhexp3.SetLineColor(ROOT.kBlue+3);
hhexp0.SetLineStyle(2);
hhexp1.SetLineStyle(2);
hhexp2.SetLineStyle(2);
hhexp3.SetLineStyle(2);
hhobs0.SetLineColor(ROOT.kBlue+3);
hhobs1.SetLineColor(ROOT.kBlue+3);
hhobs2.SetLineColor(ROOT.kBlue+3);
hhobs3.SetLineColor(ROOT.kBlue+3);
hhobs0.SetLineStyle(1);
hhobs1.SetLineStyle(1);
hhobs2.SetLineStyle(1);
hhobs3.SetLineStyle(1);


canv = ROOT.TCanvas("AZh2HDM","AZh2HDM")
pads = plot.TwoPadSplit(0.8, 0, 0)
pads[1].cd()
pads[1].SetLogz(1)
XSTimesBR_A.SetStats(0)
XSTimesBR_A.SetTitle("")
XSTimesBR_A.GetXaxis().SetTitle("cos(#beta-#alpha)")
XSTimesBR_A.GetYaxis().SetTitle("tan(#beta)")
XSTimesBR_A.GetZaxis().SetTitle("#sigma(ggA)*BR(A#rightarrowZh#rightarrowll#tau#tau) (pb)")
XSTimesBR_A.GetZaxis().SetTitleOffset(1.5)
XSTimesBR_A.GetZaxis().SetRangeUser(0.00005,0.1);
XSTimesBR_A.SetContour(255)
XSTimesBR_A.Draw("COLZ")
zhexp0.Draw("LSAME")
zhexp1.Draw("LSAME")
zhexp2.Draw("LSAME")
zhobs0.Draw("LSAME")
zhobs1.Draw("LSAME")
zhobs2.Draw("LSAME")


pads[0].cd()

plot.Set(h_top.GetXaxis(), LabelSize=0, TitleSize=0, TickLength=0)
plot.Set(h_top.GetYaxis(), LabelSize=0, TitleSize=0, TickLength=0)
h_top.Draw()

legend = plot.PositionedLegend(0.4, 0.08, 3, 0.015)
plot.Set(legend, NColumns=2, Header='#bf{%.0f%% CL Excluded:}' % (0.95*100.))
legend.SetFillStyle(0)
legend.SetBorderSize(0)
legend.AddEntry(zhexp0, "Expected","L")
legend.AddEntry(zhobs0, "Observed","L")
legend.Draw()

latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.04)
latex.DrawLatex(0.155, 0.85, "2HDM Type-II")
latexsplit = ROOT.TLatex()
latexsplit.SetNDC()
latexsplit.SetTextSize(0.025)
latexsplit.DrawLatex(0.155, 0.82, "m_{H} = m_{A} = 300 GeV")



canv.Print('.pdf')
canv.Print('.png')
canv.Close()

canv2 = ROOT.TCanvas("Hhh2HDM","Hhh2HDM")
pads2 = plot.TwoPadSplit(0.8, 0, 0)
pads2[1].cd()
pads2[1].SetLogz(1)
XSTimesBR_H.SetStats(0)
XSTimesBR_H.SetTitle("")
XSTimesBR_H.GetXaxis().SetTitle("cos(#beta-#alpha)")
XSTimesBR_H.GetYaxis().SetTitle("tan(#beta)")
XSTimesBR_H.GetZaxis().SetTitle("#sigma(ggH)*BR(H#rightarrowhh#rightarrowbb#tau#tau) (pb)")
XSTimesBR_H.GetZaxis().SetTitleOffset(1.5)
XSTimesBR_H.GetZaxis().SetRangeUser(0.001,1);
XSTimesBR_H.SetContour(255)
XSTimesBR_H.Draw("COLZ")
hhexp0.Draw("LSAME")
hhexp1.Draw("LSAME")
hhexp2.Draw("LSAME")
hhexp3.Draw("LSAME")
hhobs0.Draw("LSAME")
hhobs1.Draw("LSAME")
hhobs2.Draw("LSAME")
hhobs3.Draw("LSAME")


pads2[0].cd()
h_top.Draw()

legend2 = plot.PositionedLegend(0.4, 0.08, 3, 0.015)
plot.Set(legend2, NColumns=2, Header='#bf{%.0f%% CL Excluded:}' % (0.95*100.))
legend2.SetFillStyle(0)
legend2.SetBorderSize(0)
legend2.AddEntry(hhexp0, "Expected","L")
legend2.AddEntry(hhobs0, "Observed","L")
legend2.Draw()

latexhh = ROOT.TLatex()
latexhh.SetNDC()
latexhh.SetTextSize(0.04)
latexhh.DrawLatex(0.155, 0.85, "2HDM Type-II")
latexhhsplit = ROOT.TLatex()
latexhhsplit.SetNDC()
latexhhsplit.SetTextSize(0.025)
latexhhsplit.DrawLatex(0.155, 0.82, "m_{H} = m_{A} = 300 GeV")



canv2.Print('.pdf')
canv2.Print('.png')
canv2.Close()

