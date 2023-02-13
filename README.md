# Food-Spoilage-Detection-System
In today's world, even after so much advancement in technology, a lot of death occurs due to food poisoning. Bacteria and other harmful microorganisms can't be detected through naked eyes and by their odour. Most of the people trust their vendor and they simply purchase the contaminated food. Many of us don't have enough time to check for each and every single fruit and food. 
Therefore we have come up with a innovative solution for all these problems.








By carefully observing the contaminated food and performing various tests on them, we have come up few conclusions:
1. Outer appearance of the food completely changes once they are spoilt.
2. Spoilt food produces pungent odour.
3. Oxygen level decreases around the contaminated food as bacteria consumes more oxygen.
4. Concentration of few gases such as Ammonia increases near the spoilt food.






As per the solution is concerned we have built a machine learning model that will scan the images of the food and categorise them whether they are spoilt or not. 
We have used CNN(CONVOLUTION NEURAL NETWORK) for this purpose. The reason why CNN is chosen over ANN is because:
1. Hardware Dependence:
•Artificial Neural Networks require processors with parallel processing power, by their structure.
•For this reason, the realization of the equipment is dependent.
2. Unexplained functioning of the network:
•This the most important problem of ANN.
•When ANN gives a probing solution, it does not give a clue as to why and how.
•This reduces trust in the network.
3. Assurance of proper network structure:
•There is no specific rule for determining the structure of artificial neural networks.
•The appropriate network structure is achieved through experience and trial and error.
4. The difficulty of showing the problem to the network:
•ANNs can work with numerical information.
•Problems have to be translated into numerical values before being introduced to ANN.
•The display mechanism to be determined will directly influence the performance of the network.
•This is dependent on the user's ability.
5. The duration of the network is unknown:
•The network is reduced to a certain value of the error on the sample means that the training has been completed.
•The value does not give us optimum results.

Now if we talk about CNN, it has got some advantages over other neural networks. Such as:
Over the years, research on convolutional neural networks (CNNs) has progressed rapidly, however the real-world deployment of these models is often limited by computing resources and memory constraints. What has also led to extensive research in ConvNets is the accuracy of difficult classification tasks that require understanding abstract concepts in images.

Another reason why CNN are hugely popular is because of their architecture, the best thing is there is no need for feature extraction. The system learns to do feature extraction and the core concept of CNN is, it uses convolution of image and filters to generate invariant features which are passed on to the next layer. The features in next layer are convoluted with different filters to generate more invariant and abstract features and the process continues till one gets final feature / output (let say face of X) which is invariant to occlusions.

Also, another key feature is that deep convolutional networks are flexible and work well on image data.  As one researcher points out, convolutional layers exploit the fact that an interesting pattern can occur in any region of the image, and regions are contiguous blocks of pixels.  But one of the reasons why researchers are excited about deep learning is the potential for the model to learn useful features from raw data. Now, convolutional neural networks can extract informative features from images, eliminating the need of traditional manual image processing methods.

Our model can detect food spoilage in various fruits such as apples, bananas,etc. We have used more than 12000 images to train our model. As a result our model has an accuracy of over 97 percentage. You can surely rely on it.

For the future aspect, in order to improve the result, we are planning to include temperature sensor, oxygen level measuring device, ammonia detector as well as odour detector.

We will fit all these devices with our machine learning model and sell it to vendors. The whole system will be fully automated. It will scan the foods at real time and predict whether quality of food.
