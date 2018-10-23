<html>
    <h1>Purposes of this assignment is to give you experience of the following:</h1>
    <ul>
      <li> implementing software given a design/specification</li>
      <li> programming algorithms using lists and tuples </li>
      <li> working with unit tests and test-driven developement </li>
      <li> devising your own mathematical model/solution of a problem and implementing it </li>
      <li> refactoring existing designs/specifications </li>
    </ul>
    <h1>General idea of the assignment</h1>
    <p>Write a program to play the game of <a href="http://en.wikipedia.org/wiki/Three_Musketeers_%28game%29">Three
        Musketeers</a>--human against computer.</p>
    <p>You have probably never heard of this game. That's okay, the rules are
      simple -- that's why we chose it. The link above is to a Wikipedia article
      that explains the game, and we can answer questions if necessary.</p>
    <h1>Details</h1>
    <h2>Get starter files and put them in a GitHub repository</h2>
    Get the files <code>three_musketeers.py</code> and <code>test_three_musketeers.py</code>
    to your computer and push them to the repository that you created and set up (see the  
    guiding docs)<br />
    <h2>Write few initial tests first</h2>
    <p> Remember that you should follow the TDD approach in this project. Thus, first insert some initial
    tests for every (fruitful) function. Simply go through the file <code>test_three_musketeers.py</code>
    and make sure that there is one test everywhere you see <code># Replace with tests</code>. You will 
    add more tests at the later stages of the project. </p>
    <h2>Write initial implementation</h2>
    <p>
    Go through the file <code>three_musketeers.py</code> and create initial implementation for each
    function. Essentially, you need to create a stub for each function, i.e., a return value that makes
    sense but may be incorrect. (For example, where an integer should be returned, return 0, and where
    a list should be returned, return [].) 
    </p>
    <p> 
    You should not spend much time on the two stages above. You will provide more detailed tests
    and correct implementation later. The results of your work here should be
    committed in your repository by the deadline of Session 7.
    </p>
    <h2>Add more tests and function implementations in the TDD loop</h2>
    <p>
    Gradually increase the number of tests and improve your implementations. You have time until the
    project deadline to do that, however, we recommend you to have all the tests and the program 
    correctly working at most one month before that so that you have sufficient time to work on
    strategies and extention with files (if you do not want to skip them). The results of your work 
    should be stored in the file <code>three_musketeers.py</code>
    and the tests in <code>test_three_musketeers.py</code>. 
    </p>
    <h2>Extend your program with strategies</h2>
    <p>The computer does <strong>not</strong> have to play a great game--it does have to
      play legally. However, if the computer plays stupidly, it won't be much
      fun. If you would like to implement a simple strategy, here's a start:</p>
    <ul>
      <li>The three Musketeers should try to stay as far away from one another
        as possible. </li>
      <li>Cardinal Richelieu's men should try to all move in the same direction.</li>
    </ul>
    Think how to define those strategies in a precise way, how to express them in algorithms, and implement them. 
    The results of your work
    after this stage should be stored in the file <code>three_musketeers_with_strategies.py</code>
    and the (additional) tests in <code>test_three_musketeers_with_strategies.py</code>.
    </p>  
    <h2>Extend your program with files</h2>
    <p> As you see, the original specification does not include an option for a user to save
    the game state and to start playing from it later. Therefore, you can add the functionality to the
    system that would allow to ask of a user at any point when its his/her move, whether he/she wants
    to save the game to a file and exit. On the other hand, before the beginning of a game, the system 
    can ask the user whether he/she wants to play from scratch, or load a previous game. You are free
    to define yourself how this should work and change any part of the original specification to 
    achieve your goals. The results of your work
    after this stage should be stored in the file <code>three_musketeers_with_files.py</code>. New tests are 
    not required for this stage of the project.
    </p>
    <h2>What you are required to do</h2>
    <p>
    We understand that you may be short of time during the term to do all of the above. Therefore, we only
    require that you complete "Get starter files and put them in a GitHub repository", "Write few initial tests first",
    "Write initial implementation" and "Add more tests and function implementations in the TDD loop"
    stages of the project. With them you will get up to 70% of the full project mark. Then, you can chose whether
    to add "Extend your program with strategies" (adds up to 30%) or "Extend your program with files" (adds up to 30%). Extending
    your program with either of the latter two features in optional (but required if you want to get more than 70% of the
    maximal project mark). Of course, you are welcome to do both extentions. In that case, we will provide feedback on both of them
    but will consider only one of them for marking (the one that is better in our opinion). Therefore, it is better to implement
    one extension very well than two of them weakly.    
    </p>
    <h2>How your work will be marked</h2>
    <p> Firstly, we use the common criteria for marking code:
    <ul>
      <li>Readability and Clarity (use comments when your code does something non-trivial)</li>
      <li>Completeness of the Implementation and Tests (every required function and feature must be implemented)</li>
      <li>Correctness (everything your implement must return correct and expected results)</li>
    </ul>
    In addition, the style of work will be affect your mark, which adds one more criteria:
    <ul>
      <li> Consistency of commit history in git (you must start working on the project by the deadline of Session 7
      and do some commits every week or two; the projects where the first and the last commits are a couple of days
      before the deadline are unlikely to be given a high mark)</li>
    </ul>
    </p>
    <h2>About the provided code </h2>
    <p>See the <a href="http://en.wikipedia.org/wiki/Three_Musketeers_%28game%29">Wikipedia
        article</a> for the rules of the game.</p>
    <p>The "board" is represented as a list of five lists; each of these lists
      represents a row, and each list contains five elements. The first list
      represents the first row; the first element in each list represents the
      first column. The values in the list must each be one of three things: an
      <code>'M'</code>, representing a Musketeer, an <code>'R'</code>,
      representing one of Cardinal Richelieu's men; and a <code>'-'</code>,
      representing an empty space. <code>board</code> is a
      global variable in this program.</p>
    <p>Directions are given as one of the four strings <code>'left'</code>, <code>'right'</code>,
      <code>'up</code>', and <code>'down'</code>.</p>
    <p>Your job is to complete the program,  both <code>three_musketeers.py</code>
      and <code>test_three_musketeers.py</code>.</p>
    <ul>
      <li>In <code>three_musketeers.py</code>,
        <ul>
          <li>We use a global variable <code>board</code> to store the current state of 
            the game, and all the functions have access to it.
          <li>For some functions, we indicate that their supplied arguments will not necessarily be 
            in correct value ranges (for the other functions, you can assume that they are in 
            the correct ranges). In this case, you must check for the correctness of the arguments
            and raise an exception if this is violated. Also, the corresponding test methods must
            test the calls with the incorrect arguments and verify if the exceptions are raised.
          <li>The <code>pass</code> statement does nothing. You should replace
            every <code>pass</code> statement with actual code. In the beginning, provide stubs, i.e., 
            return some syntactically correct possibly constant values that do not need to be correct
            semantically. Further, as you develop your project, you will replace them with the code
            that works better and better and covers more and more test cases.</li>
        </ul>
      </li>
      <li>In <code>test_three_musketeers.py</code>,
        <ul>
          <li> Call the function <code>set_board(new_board)</code> to get a fresh new
            <code>board</code> before every test. Do that so that the result of one
            test does not depend on what other tests may have done. (You shoud use
            at least two initial test board.)</li>
          <li>The test functions are not complete (some of them are empty). It is your job
          to fill them in with reasonable tests. In the beginning, just make sure that there
          is at least one test in each of the test functions. Further, as you develop the project, increase
          the number of tests. It is your decision which tests and how many to include, but the tests for 
          each function must reflect the variety of its use cases (including exceptions if we
          indicated that the function must raise them). I would expect between 5 and 10 tests for each
          function, depending on how much the function does.</li>
        </ul>
      </li>
    <li> Try not to work on <code>three_musketeers.py</code> and <code>test_three_musketeers.py</code> 
        in isolation and follow the TDD approach. After improving your code, increase test cases for it, 
        then improve it further, etc. 
    </ul>
    <h2>Some brief Python reminders </h2>
    <p>Here are some Python things to remember:</p>
    <ul>
      <li>Methods can call other methods. Sometimes this means that a fairly
        complex job can be accomplished in just a line or two.</li>
      <li>It's easy to get things in and out of tuples. If <code>location</code>
        is a two-tuple, all of the following work:
        <ul>
          <li><code>(row, column) = location</code></li>
          <li><code>location = (row, column)</code></li>
          <li><code>column = location[1]</code></li>
        </ul>
      </li>
      <li>Although you can sometimes leave the parentheses off a tuple, you must
        have them when calling a function: do_something((3, 4))</li>
      <li>Sequences of the same type can be "added." For example, <code>[1, 2]
          + [3, 4]</code> gives <code>[1, 2, 3, 4]</code>.</li>
      <li><code>append</code> adds an element to a sequence. For example, if <code>a
          = [1, 2]</code>, <code>a.append(3)</code> changes <code>a</code> to
        <code>[1, 2, 3]</code>.</li>
      <li>If <code>b</code> is a list of lists, <code>b[0]</code> is the first
        list, and <code>b[0][0]</code> is the first element in the first list.
        For example, if <code>c</code> is <code><nobr>[[1, 2], [3, 4, 5]]</nobr></code>,
        then <code>c[1][2]</code> is <code>5</code>.</li>
    </ul>
    <h2>Code and Documentation </h2>
    <p> We do not require any documentation from you but you should make sure we understand
    what your code does. Therefore, use the comments inside your code. Comment on every piece of
    code that does something not trivial. It is sufficient that you submit the files specified above,
    however, if you wish, you can supply other (textual) files or overwrite this <code>readme.md</code>
    file with any description you consider useful.</p>
    <h2>Submission</h2>
    <p>You will be working in Git and your last commit before the project submission deadline will
    be considered as your final submission. If we see that you have commits after the deadline, by default
    we will mark the last commit you made before the deadline. If you prefer us to mark your work as a late 
    submission instead (possibly providing mitigating circumstances to avoid the cap on the mark), contact
    us to tell about that.</p>
    <p>As with the exercise sheets, for the accountancy reasons, we require that you 
    "back up" your project files on Moodle via an assignment link provided on the project Moodle page. 
    If it is not there yet, it will appear in a couple of days. You simply need to upload the final 
    version of all your files there. You need to do it <strong>only once</strong> when your
    project is in the final version and before the submittion deadline.</p>
    
 </html>
