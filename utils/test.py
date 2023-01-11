import hrtf

cipic = hrtf.CipicHRTF('../data/subject_003.sofa', 44100.0)
print(cipic.azimuths.shape)
print(cipic.elevations.shape)
