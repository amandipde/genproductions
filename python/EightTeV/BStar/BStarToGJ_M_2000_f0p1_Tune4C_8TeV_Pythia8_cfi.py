import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

generator = cms.EDFilter("Pythia8GeneratorFilter",
                  pythiaPylistVerbosity = cms.untracked.int32(0),
                  filterEfficiency = cms.untracked.double(1.0),
                  pythiaHepMCVerbosity = cms.untracked.bool(False),
                  comEnergy = cms.double(8000.0),
                  maxEventsToPrint = cms.untracked.int32(0),
                  crossSection = cms.untracked.double(0.000001003),
                  PythiaParameters = cms.PSet(
                        processParameters = cms.vstring(

                            'Main:timesAllowErrors = 10000',
                            'ParticleDecays:limitTau0 = on',
                            'ParticleDecays:tau0Max = 10',
                            'ExcitedFermion:bg2bStar = on',
                            '4000005:m0 = 2000.',
                            '4000005:onMode = off',
                            '4000005:onIfMatch = 22 5',
                            'ExcitedFermion:Lambda = 2000.',
                            'ExcitedFermion:coupFprime = 0.1',
                            'ExcitedFermion:coupF = 0.1',
                            'ExcitedFermion:coupFcol = 0.1',
                            'Tune:pp 5',
                            'Tune:ee 3'
                            ),
                        parameterSets = cms.vstring('processParameters')
                  )
)
