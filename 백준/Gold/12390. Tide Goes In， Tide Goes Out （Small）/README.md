# [Gold IV] Tide Goes In, Tide Goes Out (Small) - 12390 

[문제 링크](https://www.acmicpc.net/problem/12390) 

### 성능 요약

메모리: 35016 KB, 시간: 64 ms

### 분류

너비 우선 탐색, 데이크스트라, 그래프 이론, 그래프 탐색, 최단 경로

### 제출 일자

2025년 11월 13일 16:23:37

### 문제 설명

<p>You are kayaking through a system of underground caves and suddenly realize that the tide is coming in and you are trapped! Luckily, you have a map of the cave system. You are stuck until the tide starts going out, so you will be here for a while. In the meantime, you want to determine the fastest way to the exit once the tide starts going out.</p>

<p>The cave system is an <strong>N</strong> by <strong>M</strong> grid. Your map consists of two <strong>N</strong> by <strong>M</strong> grids of numbers: one that specifies the height of the ceiling in each grid square, and one that specifies the height of the floor in each grid square. The floor of the cave system is porous, which means that as the water level falls, no water will remain above the water level.</p>

<p>You are trapped at the north-west corner of the map. The current water level is <strong>H</strong>centimeters, and once it starts going down, it will drop at a constant rate of 10 centimeters per second, down to zero. The exit is at the south-east corner of the map. It is now covered by water, but it will become passable as soon as the water starts going down.</p>

<p>At any time, you can move north, south, east or west to an adjacent square with the following constraints:</p>

<ul>
	<li>The water level, the floor height of your current square, and the floor height of the adjacent square must all be at least 50 centimeters lower than the ceiling height of the adjacent square. Note: this means that you will never be able to enter a square with less than 50 centimeters between the floor and the ceiling.</li>
	<li>The floor height of the adjacent square must be at least 50 centimeters below the ceiling height of your current square as well.</li>
	<li>You can never move off the edge of the map.</li>
</ul>

<p>Note that you can go up or down as much as you want with your kayak. (You're very athletic from all this kayaking!) For example, you can go from a square with floor at height 10 centimeters to an adjacent square with floor at height 9000 centimeters (assuming the constraints given above are met).</p>

<p> </p>

<p>These constraints are illustrated below: <img src="https://onlinejudgeimages.s3.amazonaws.com/problem/12390/images-48.png" style="vertical-align:middle"></p>

<ul>
	<li>In the first image, you can't move to the right because the water level is less than 50 centimeters below the ceiling height of the adjacent square.</li>
	<li>In the second image, you can't move to the right because the floor height of your current square is less than 50 centimeters below the ceiling height of the adjacent square.</li>
	<li>In the third image, you can't move to the right because the floor height of the adjacent square is less than 50 centimeters below the ceiling height of the adjacent square. You'll never be able to enter that square from any direction.</li>
	<li>In the fourth image, you can't move to the right because the floor height of the adjacent square is less than 50 centimeters below the ceiling height of the current square.</li>
</ul>

<p> </p>

<p>When moving from one square to another, if there are at least 20 centimeters of water remaining on the current square when you start moving from it, it takes 1 second to complete the move (you can use your kayak). Otherwise, it takes 10 seconds (you have to drag your kayak). Note that the time depends only on the water level in the square you are leaving, not in the square you are entering.</p>

<p>It will be a while before the tide starts going out, and so you can spend as much time moving as you want before the water starts going down. What matters is how much time you will need from the moment the water starts going down until the moment you reach the exit. Can you calculate this time?</p>

### 입력 

 <ul>
	<li>The first line will contain a single integer, <strong>T</strong>: the number of test cases </li>
	<li>It is followed by <strong>T</strong> test cases, each starting with a line containing integers <strong>H</strong>, <strong>N</strong> and <strong>M</strong>, representing the initial water level height, in centimeters, and the map dimensions. The following 2<strong>N</strong> lines contain the ceiling and floor heights as follows:
	<ul>
		<li>The next <strong>N</strong> lines contain <strong>M</strong> space-separated integers each. The <em>j</em>th integer in the <em>i</em>th row represents <strong>C<sub>ij</sub></strong>, the height of the ceiling in centimeters at grid location <em>(j, i)</em>, where increasing <em>i</em> coordinates go South, and increasing <em>j</em>coordinates go East.</li>
		<li>The next <strong>N</strong> lines contain <strong>M</strong> space-separated integers representing the heights of the floor, in the same format.</li>
	</ul>
	</li>
	<li>At the starting location, there will always be at least 50 cm of air between the ceiling and the starting water level, and at least 50 cm between the ceiling and the floor.</li>
	<li>The exit location will always have at least 50 cm of air between the ceiling and the floor.</li>
	<li>There will always be a way out (you got in, after all!).</li>
</ul>

<h3>Limits</h3>

<ul>
	<li>1 ≤ <strong>T</strong> ≤ 50. </li>
	<li>1 ≤ <strong>N, M</strong> ≤ 10. </li>
	<li>1 ≤ <strong>H</strong> ≤ 1000. </li>
	<li>1 ≤ <strong>F<sub>xy</sub></strong> ≤ <strong>C<sub>xy</sub></strong> ≤ 1000.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: t", where x is the case number (starting from 1), and t is the time, in seconds, starting from when the tide begins going out, that it takes you to make your way out of the cave system. Answers within an absolute or relative error of 10<sup>-6</sup> of the correct answer will be accepted.</p>

