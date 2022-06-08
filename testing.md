* [**Testing**](<#testing>)
* [**Manual Testing**](<#manual-testing>)
* [**Bugs**](<#bugs>)
* [**Accessibilty**](<#accessibilty>)
# Testing
W3C markup validator and W3C CSS validator were used to test and vailidate all the code on all 4  pages of history quiz to ensure that there were no syntax errors. JS hint was used to test the Javascrpit code.


 # index
 The image below is testing for the index.html file. No errors or warnings are visable. 

![Testing on W3C Html](assets/images/htmlin.png)

![Testing on W3C CSS](assets/images/homecss.png)

 # Instructions
 The image below is testing for the instructions.html file. No errors or warnings are visable. 

![Testing on W3C Html](assets/images/inshtml.png)

![Testing on W3C CSS)](assets/images/incss.png)

 # Game
 The image below is testing for the game.html file. No errors or warnings are visable. 

![Testing on W3C Html and CSS](assets/images/gamehtml.png)

![Testing on W3C CSS)](assets/images/gamecss.png)
 # Score
 The image below is testing for the Score.html file. No errors or warnings are visable. 

![Testing on W3C Html](assets/images/shtml.png)

![Testing on W3C CSS](assets/images/scorecss.png)

# Manual Testing/ Devlepoment

### Html and css Tests
|  Test  | Issues/Bugs  | Solution   | Functional  |
|--------|--------|--------|--------|
| Button positioning and size | Buttons would not appear in the correct area or seemed to be too big for the container| All the buttons were placed into an id element and configured with CSS. This was done by using display function with an inline table to solve the issue  |All tests ran with no issues on different devices.|
| Button positioning and size  |  Lets begin button would appear on the right hand side, of the screen|Image width chnaged from 80% to 100% which moved the lets begin button back to its orginal posistion|Button appears in the correct postiion|
|Colour contrasts|Colour contrasts came in at 2.95. this caused issues with accessibility|The entire colour scheme has been changed from orange and white to orange and blue (two different shades of blue)|Ran through lighthouse contrast came out at 8.33. colour chnaged to white and copper colour   |
|Buttons links|When testing the site, the button wouldn’t  change to the different pages on the website|When reviewing the code for the href elements. I noticed that due to a change in the file names i haven’t change to src links to account for the new file names|All links tested and working fine|
|Html closing tag|Missing html closing tag on index.html page|Closing tag added|Test and no issues appeared on w3 validator.|

### Javascript tests
|Test| Issues/Bugs|Solutions|Functional|
|----|------------|---------|----------|
|JavaScript answers|While testing the quiz to see if the answer would run. I noticed that answers would not load up correctly.|While reviewing the answers on the JavaScript I noticed that I had used a single quotation mark instead of a double quotation mark this caused the answer not to load. All changed|Testing the quiz all question loaded up and ran with no issues.|
|JavaScript setTimeOut()|Timer set to 0.06  which is incorrect, cannot detected bugs as the timer changes questions to quickly.|Timer changed to 1000, this will allow test to be carried out, to see if there are any bugs|Timer changed, no bugs or issues found|
|Colour change on answers (Javascript function)  |Colours for incorrect and correct answers would not change, when you selected your answer.|Problem solved, this was achived by adding a line of code to the javascript file| All questions tested,  colour change on questions now appears.|
|Progress bar|Game test by playing the quiz, the progress bar fills up as you complete the 10 questions|No issues found| No fixes needed.|
|Score counter|Score counter test by playing the game, this tested by selecting the correct and incorrect answers. Colour chanage functions wasnt working.|Colour function for incorrect and correct answer now fully functioning.|Line of javascrpit code added to the make colour change function work.|
### Responisveness Testing
| Test Responsiveness | Issues Type     | Solutions | Functional |
|---------------------|-----------------|-----------|------------|
| Iphone 5            | No Issues seen  | N/A       | Pass       |
| Iphone 6            | No issues Seen  | N/A       | Pass       |
| Iphone 8/9/10       | No Issues seen  | N/A       | Pass       |
| Screen Size 768px   | No Issues seen  | N/A       | Pass       |
| Screen Size 1024px  | No Issues seen  | N/A       | Pass       |
| Ipad                | No issues seen  | N/A       | Pass       |

![Responsiveness](assets/images/imr1.png)
![Responsiveness](assets/images/imr2.png)

### Deployed Testing
| Test                              | Outcome                                                     | Result                                                    |
|-----------------------------------|-------------------------------------------------------------|-----------------------------------------------------------|
| Check against development version | Has the testing criteria been applied to deployed version   | Pass, No Issues                                           |
| visual Check                      | All visual checks carried out on full deployment version?   | Pass                                                      |
| Code checked                      | Has the code been checked for errors?                       | Code check and ran through w3 validator and CSS validator |

### User Feedback Testing 
| User Feedback | Result  |
|---------------|---------|
|I want a quiz that provides rules and instructions on how to play the game.|Achieved|
|I want to be able to play the game either on laptop or on my phone.|Achieved|
|I would like to know where abouts on the page im on.|Achieved|
|I would have like the questions to appear randomised every time I play so I am not answering the same questions every time I play.|Achieved|
|I would like to have feedback on the questions i got correct or incorrect, some kind of idenifcation of the correct or incorrect answers would be greatly appreciated.|Achieved|

![Instructions](assets/images/submit2.PNG)
![Home](assets/images/submit1.PNG)
![User Feed Back Changes](assets/images/home1.PNG)
![User Feed Back Changes](assets/images/ins.PNG)
![User Feed Back Changes](assets/images/score1.PNG)
![User Feed Back Changes](assets/images/test1.png)
![User Feed Back Changes](assets/images/test2.png)
# BUGS
The orginal design for the history quiz has changed a lot due to bugs and learning curves i faced during the development of this project. 

  1. color change when user selects wrong answer  does not activate. This has now been fixed.
  2. Question choices appear to small on smaller devices they do not fill up the full page. Boxes now fill up the screen, small editing reuqired on css file.
  3. Timer does not function correclty after 60seconds. questions should have skip once the timer has ran out.
  4. During testing users score didnt save feature removed.

# Accessibilty
Accessibilty was tested on lighthouse during the development of  history quiz. The results are distheplayed below.

![Accessibilty Testing](assets/images/quizlight.png)

