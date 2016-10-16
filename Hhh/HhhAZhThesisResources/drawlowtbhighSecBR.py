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


set_plot_style()
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



f1 = ROOT.TFile("../../../auxiliaries/models/low-tb-high_8TeV.root")
hist_XSA = f1.Get("xs_gg_A")
hist_BRAZh = f1.Get("br_A_Zh")
hist_BRhtautau = f1.Get("br_h_tautau")
hist_XSH = f1.Get("xs_gg_H")
hist_BRHhh = f1.Get("br_H_hh")
hist_BRhbb = f1.Get("br_h_bb")

f2 = ROOT.TFile("AZhContourslowtb.root")
#f3 = ROOT.TFile("cmb_2HDMtyp2-cosba-tanb-azh.root")

#tree = f1.Get("Tree2HDM");

azhexp0_pre = f2.Get("cont_exp0_0")
azhobs_pre = f2.Get("cont_obs_0")

npoints_exp = azhexp0_pre.GetN()
exp0_xes = azhexp0_pre.GetX()
exp0_ys = azhexp0_pre.GetY()
for i in range (0,npoints_exp):
  exp0_xes[i]+=5

npoints_obs = azhobs_pre.GetN()
obs_xes = azhobs_pre.GetX()
obs_ys = azhobs_pre.GetY()
for i in range (0,npoints_obs):
  obs_xes[i]+=5


azhexp0 = ROOT.TGraph(npoints_exp,exp0_xes,exp0_ys)
azhobs = ROOT.TGraph(npoints_obs,obs_xes,obs_ys)

#hhexp0 = f2.Get("cmb/gr_expected_0")
#hhexp1 = f2.Get("cmb/gr_expected_1")
#hhexp2 = f2.Get("cmb/gr_expected_2")
#hhexp3 = f2.Get("cmb/gr_expected_3")
#hhobs0 = f2.Get("cmb/gr_observed_0")
#hhobs1 = f2.Get("cmb/gr_observed_1")
#hhobs2 = f2.Get("cmb/gr_observed_2")
#hhobs3 = f2.Get("cmb/gr_observed_3")

#zhexp0 = f3.Get("cmb/gr_expected_0")
#zhexp1 = f3.Get("cmb/gr_expected_1")
#zhexp2 = f3.Get("cmb/gr_expected_2")
#zhobs0 = f3.Get("cmb/gr_observed_0")
#zhobs1 = f3.Get("cmb/gr_observed_1")
#zhobs2 = f3.Get("cmb/gr_observed_2")



ybins = np.array([0.95,1.05,1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15,2.25,2.35,2.45,2.55,2.65,2.75,2.85,2.95,3.05,3.15,3.25,3.35,3.45,3.55,3.65,3.75,3.85,3.95,4.05])
XSTimesBR_A = ROOT.TH2F("XSTimesBR_A","XSTimesBR_A",130,220,350,30, ybins)
XSTimesBR_H = ROOT.TH2F("XSTimesBR_H","XSTimesBR_H",130,220,350,30, ybins)
h_top = ROOT.TH2F("htop","htop",130,220,350,30,ybins)
h_top.SetTitle("")
h_top.SetStats(0)


for i in range (1,131):
  for j in range (1,41):
    xsA = hist_XSA.GetBinContent(hist_XSA.GetXaxis().FindBin(XSTimesBR_A.GetXaxis().GetBinCenter(i)),hist_XSA.GetYaxis().FindBin(XSTimesBR_A.GetYaxis().GetBinCenter(j)))
    brA = hist_BRAZh.GetBinContent(hist_BRAZh.GetXaxis().FindBin(XSTimesBR_A.GetXaxis().GetBinCenter(i)),hist_BRAZh.GetYaxis().FindBin(XSTimesBR_A.GetYaxis().GetBinCenter(j)))
    xsH = hist_XSH.GetBinContent(hist_XSH.GetXaxis().FindBin(XSTimesBR_A.GetXaxis().GetBinCenter(i)),hist_XSH.GetYaxis().FindBin(XSTimesBR_A.GetYaxis().GetBinCenter(j)))
    brH = hist_BRHhh.GetBinContent(hist_BRHhh.GetXaxis().FindBin(XSTimesBR_A.GetXaxis().GetBinCenter(i)),hist_BRHhh.GetYaxis().FindBin(XSTimesBR_A.GetYaxis().GetBinCenter(j)))
    brhtautau = hist_BRhtautau.GetBinContent(hist_BRhtautau.GetXaxis().FindBin(XSTimesBR_A.GetXaxis().GetBinCenter(i)),hist_BRhtautau.GetYaxis().FindBin(XSTimesBR_A.GetYaxis().GetBinCenter(j)))
    brhbb = hist_BRhbb.GetBinContent(hist_BRhbb.GetXaxis().FindBin(XSTimesBR_A.GetXaxis().GetBinCenter(i)),hist_BRhbb.GetYaxis().FindBin(XSTimesBR_A.GetYaxis().GetBinCenter(j)))
    XSTimesBR_A.SetBinContent(i,j,xsA*brA*brhtautau*0.10099)
    XSTimesBR_H.SetBinContent(i,j,xsH*brH*brhtautau*brhbb*2)


azhexp0.SetLineColor(ROOT.kBlue+3)
azhexp0.SetLineWidth(2)
azhexp0.SetLineStyle(2)
azhobs.SetLineColor(ROOT.kBlue+3)
azhobs.SetLineStyle(1)
azhobs.SetLineWidth(2)


canv = ROOT.TCanvas("AZhlowtbhigh","AZhlowtbhigh")
pads = plot.TwoPadSplit(0.8, 0, 0)
pads[1].cd()
pads[1].SetLogz(1)
XSTimesBR_A.SetStats(0)
XSTimesBR_A.SetTitle("")
XSTimesBR_A.GetXaxis().SetTitle("m_{A} [GeV]")
XSTimesBR_A.GetYaxis().SetTitle("tan(#beta)")
XSTimesBR_A.GetZaxis().SetTitle("#sigma(ggA)*BR(A#rightarrowZh#rightarrowll#tau#tau) (pb)")
XSTimesBR_A.GetZaxis().SetTitleOffset(1.5)
XSTimesBR_A.SetContour(255)
XSTimesBR_A.GetZaxis().SetRangeUser(0.0005,0.1);
XSTimesBR_A.Draw("COLZ")
azhexp0.Draw("LSAME")
azhobs.Draw("LSAME")


pads[0].cd()
plot.Set(h_top.GetXaxis(), LabelSize=0, TitleSize=0, TickLength=0)
plot.Set(h_top.GetYaxis(), LabelSize=0, TitleSize=0, TickLength=0)
h_top.Draw()

legend = plot.PositionedLegend(0.4, 0.08, 3, 0.015)
plot.Set(legend, NColumns=2, Header='#bf{%.0f%% CL Excluded:}' % (0.95*100.))
legend.SetFillStyle(0)
legend.SetBorderSize(0)
legend.AddEntry(azhexp0, "Expected","L")
legend.AddEntry(azhobs, "Observed","L")
legend.Draw()
#
latex = ROOT.TLatex()
latex.SetNDC()
latex.SetTextSize(0.03)
latex.DrawLatex(0.155, 0.85, "MSSM low tan#beta")
#
#
canv.Print('.pdf')
canv.Print('.png')
canv.Close()
##
canv2 = ROOT.TCanvas("Hhhlowtbhigh","Hhhlowtbhigh")
pads2 = plot.TwoPadSplit(0.8, 0, 0)
pads2[1].cd()
pads2[1].SetLogz(1)
XSTimesBR_H.SetStats(0)
XSTimesBR_H.SetTitle("")
XSTimesBR_H.GetXaxis().SetTitle("m_{A} [GeV]")
XSTimesBR_H.GetYaxis().SetTitle("tan(#beta)")
XSTimesBR_H.GetZaxis().SetTitle("#sigma(ggH)*BR(H#rightarrowhh#rightarrowbb#tau#tau) (pb)")
XSTimesBR_H.GetZaxis().SetTitleOffset(1.5)
XSTimesBR_H.GetZaxis().SetRangeUser(0.001,1);
XSTimesBR_H.SetContour(255)
XSTimesBR_H.Draw("COLZ")


pads2[0].cd()
h_top.Draw()

latexhh = ROOT.TLatex()
latexhh.SetNDC()
latexhh.SetTextSize(0.03)
latexhh.DrawLatex(0.155, 0.85, "MSSM low tan#beta")



canv2.Print('.pdf')
canv2.Print('.png')
canv2.Close()

