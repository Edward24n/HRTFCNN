import hrtf

cipic = hrtf.CipicHRTF('data/template.sofa', 44100.0)
# print(cipic.azimuths.shape)
# print(cipic.elevations.shape)

impulses = cipic.impulses
print(impulses.shape)
elevations = cipic.elevations
azimuths = cipic.azimuths

hrtf.create_cipic_hrtf('data/template.sofa', 'data/predict.sofa', impulses, elevations, azimuths)

# import json

# impulsesFlattened = impulses.ravel()
# impulseArray = []
# for i in range(len(impulsesFlattened)):
#     impulseArray.append(impulsesFlattened[i])

# sourcePositionArray = []
# for i in range(len(elevations)):
#     sourcePositionArray.append(elevations[i])
#     sourcePositionArray.append(azimuths[i])
#     sourcePositionArray.append(1)

# jsonData = {}

# with open("data/template.sofa.json", "r") as jsonFile:
#     jsonData = json.load(jsonFile)

# jsonData["Variables"]["Data_IR"]["Values"] = impulseArray
# jsonData["Variables"]["SourcePosition"]["Values"] = sourcePositionArray

# with open("data/template-2.sofa.json", "w") as jsonFile:
#     jsonFile.write(json.dumps(jsonData, indent = 4))
