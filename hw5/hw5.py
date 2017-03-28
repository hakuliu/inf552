from feedforward import FeedForwardNetwork
import hw5data as d
import neuralnetwork as nn
import math

trainingset = d.makeTrainingSet('downgesture_train.list')
print('training set of %d loaded.' % len(trainingset))
testset = d.makeTrainingSet('downgesture_test.list')
print('testing set of %d loaded.' % len(testset))

#d.makecsvfile(trainingset, 'wekadata.csv')

network = FeedForwardNetwork(30*32, 1, [100])
network.constructNetwork()
print('network constructed')

print('testing before training...')
tester = nn.NNTester(network, testset)
error = tester.test()
print('test error was:')
print(error)

print('beginning training...')
trainer = nn.NNTrainer(network, trainingset)
trainer.train(10)
print('training complete.')

print('testing after training...')
tester = nn.NNTester(network, testset)
error = tester.test()
print('test error was:')
print(error)
print('root-mean-square error is ')
norm = 1.0 / len(testset)
e = math.sqrt(norm * error)
print(e)