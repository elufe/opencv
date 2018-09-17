/*
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
using namespace std;

int main(int argc, char* argv[]) {
	// load an image
	cv::Mat lena = cv::imread("C:/Users/msi/Desktop/lena.png", cv::IMREAD_COLOR);

	// create a matrix for split
	cv::Mat bgr[3];

	// split image into 3 single-channel matrices
	cv::split(lena, bgr);

	// create 4 windows
	cv::namedWindow("Original Image");
	cv::namedWindow("Red Channel");
	cv::namedWindow("Green Channel");
	cv::namedWindow("Blue Channel");


	// show 4 windows
	cv::imshow("Original Image", lena);
	cv::imshow("Red Channel", bgr[2]);  // caution : the red channel index is 2!
	cv::imshow("Green Channel", bgr[1]);
	cv::imshow("Blue Channel", bgr[0]);

	cv::waitKey(0);
	return 0;
}*/
/*
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include<iostream>
#include<cstdio>


using namespace cv;
using namespace std;


int main() {

	Mat image;
	Mat cut[4];
	Mat dst[4];
	Mat bgr[3];
	Mat hist[4];
	int channel[] = { 0,1 };
	int histSize[] = { 256 };
	float range[] = { 0,256 };
	const float * ranges[] = { range };

	image = imread("C:/Users/msi/Documents/카카오톡 받은 파일/피부암 (1).jpg", CV_LOAD_IMAGE_COLOR);
	int row = image.rows; int col = image.cols;
	printf("%d %d ", row, col);





	cut[0] = image(Range(0, row / 2), Range(0, col / 2));//1사분면

	flip(image, cut[1], 1);//좌우반전
	cut[1] = cut[1](Range(0, row / 2), Range(0, col / 2)); //2사분면

	flip(image, cut[2], -1);//다 반전
	cut[2] = cut[2](Range(0, row / 2), Range(0, col / 2)); //4사분면

	flip(image, cut[3], 0);//상하반전
	cut[3] = cut[3](Range(0, row / 2), Range(0, col / 2)); // 3사분면

	for (int i = 0; i < 4; i++) cvtColor(cut[i], dst[i], CV_BGR2HSV);//CV_HSV2BGR

	for (int i = 0; i < 4; i++) calcHist(&dst[i], 1, channel, Mat(), hist[i], 1, histSize, ranges, true, false);


	double result[4][4];

	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			result[i][j] = compareHist(hist[i], hist[j], 0);

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			printf("%.6f ", result[i][j]);
		}
		cout << endl;
	}

	return 0;

}*/


#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <stdlib.h>

using namespace std;

void diff(int * width, int col) {
	for (int i = 0; i < col - 1; i++) {
		width[i] = width[i + 1] - width[i];
	}
	width[col - 1] = 0;
}

int main(int argc, char* argv[]) {
	cv::Mat image = cv::imread("C:/Users/msi/Desktop/2.jpg", cv::IMREAD_COLOR);
	int row = image.rows;//421 세로)
	int col = image.cols;//559 가로
	int a = 1, b = 1, c = 1, d = 1;
	int width[559] = { 0 };
	float width_f[624] = { 0,0 };
	int color[421][559][3] = { 0 };
	int red = 0;
	int green = 0;
	int blue = 0;
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++) {
			color[i][j][2] = image.at<cv::Vec3b>(i, j)[2];
			color[i][j][1] = image.at<cv::Vec3b>(i, j)[1];
			color[i][j][0] = image.at<cv::Vec3b>(i, j)[0];
		}
	}
	int sum_row1=0,sum_row0=0;
	for (int i = 0; i < row; i++) {
		sum_row1 += color[i][col / 2][1];
		sum_row0 += color[i][col / 2][0];
	}
	sum_row1 /= row;
	sum_row0 /= row;

	int sum_col1 = 0, sum_col0 = 0;
	for (int i = 0; i < col; i++) {
		sum_col1 += color[row/2][i][1];
		sum_col0 += color[row/2][i][0];
	}
	sum_col1 /= col;
	sum_col0 /= col;
	//중심 기준 위, 아래 조사후 가장 멀리 있는거
	int avg0 = 0;
	int avg1 = 0;

	int up = 0;

	for (int i = row / 2; i > 1; i--) {
		if (i == row / 2) {
			avg0 = (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0]);
			avg1 = (color[i - 1][col / 2][1] + color[i][col / 2][1] + color[i + 1][col / 2][1]);
		}
		else if (abs(avg0 - (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0])) > 200) {
			up = i;
			cout <<"1   "<< i << "\n";
			break;
		}
	}


	avg0 = 0;
	avg1 = 0;



	int down=0;

	for (int i = row / 2; i < row - 1; i++) {
		if (i == row / 2) {
			avg0 = (color[i - 1][col/2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0]);
			avg1 = (color[i - 1][col / 2][1] + color[i][col / 2][1] + color[i + 1][col / 2][1]);
		}
		else if (abs(avg0 - (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0])) > 100) {
			down = i;
			cout << "2   " << i << "\n";
			break;
		}
	}

	avg0 = 0;
	avg1 = 0;
	int left = 0;

	for (int j = col / 2; j > 1; j--) {
		if (j == col / 2) {
			avg0 = (color[row / 2][j-1][0] + color[row / 2][j][0] + color[row / 2][j+1][0]);
			avg1 = (color[row / 2][j-1][1] + color[row / 2][j][1] + color[row / 2][j+1][1]);
		}
		else if (abs(avg0 - (color[row / 2][j - 1][0] + color[row / 2][j][0] + color[row / 2][j + 1][0])) > 100) {
			left = j;
			cout << "3   " << j << "\n";
			break;
		}
	}



	avg0 = 0;
	avg1 = 0;
	int right = 0;

	for (int j = col / 2; j < col-1; j++) {
		if (j == col / 2) {
			avg0 = (color[row / 2][j - 1][0] + color[row / 2][j][0] + color[row / 2][j + 1][0]);
			avg1 = (color[row / 2][j - 1][1] + color[row / 2][j][1] + color[row / 2][j + 1][1]);
		}
		else if (abs(avg0 - (color[row / 2][j - 1][0] + color[row / 2][j][0] + color[row / 2][j + 1][0])) > 100) {
			right = j;
			cout << "4   " << j << "\n";
			break;
		}
	}

	avg0 = 0;
	avg1 = 0;
	int up2;
	int up3 = 999;
	for (int j = left; j < right; j++) {
		for (int i = row / 2; i > 1; i--) {
			if (i == row / 2) {
				avg0 = (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0]);
				avg1 = (color[i - 1][col / 2][1] + color[i][col / 2][1] + color[i + 1][col / 2][1]);
			}
			else if (abs(avg0 - (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0])) > 100) {
				up2 = i;
				cout << "1   " << i << "\n";
				break;
			}
		}
		if (up3 > up2)
			up3 = up2;
	}

	avg0 = 0;
	avg1 = 0;
	int down2;
	int down3 = 0;
	for (int j = left; j < right; j++) {
		for (int i = row / 2; i < row-1; i++) {
			if (i == row / 2) {
				avg0 = (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0]);
				avg1 = (color[i - 1][col / 2][1] + color[i][col / 2][1] + color[i + 1][col / 2][1]);
			}
			else if (abs(avg0 - (color[i - 1][col / 2][0] + color[i][col / 2][0] + color[i + 1][col / 2][0])) > 100) {
				down2 = i;
				cout << "2   " << i << "\n";
				break;
			}
		}
		if (down3 < down2)
			down3 = down2;
	}


	
	avg0 = 0;
	avg1 = 0;
	int left2 = 0;
	int left3 = 999;
	for (int i = up; i < down; i++) {
		for (int j = col / 2; j > 1; j--) {
			if (j == col / 2) {
				avg0 = (color[i][j - 1][0] + color[i][j][0] + color[i][j + 1][0]);
				avg1 = (color[i][j - 1][1] + color[i][j][1] + color[i][j + 1][1]);
			}
			else if (abs(avg0 - (color[row / 2][j - 1][0] + color[row / 2][j][0] + color[row / 2][j + 1][0])) > 100) {
				left2 = j;
				cout << "3   " << j << "\n";
				break;
			}

		}
		if (left3 > left2)
			left3 = left2;
	}

	avg0 = 0;
	avg1 = 0;
	int right2 = 0;
	int right3 = 0;
	for (int i = up; i < down; i++) {
		for (int j = col / 2; j < col-1; j++) {
			if (j == col / 2) {
				avg0 = (color[i][j - 1][0] + color[i][j][0] + color[i][j + 1][0]);
				avg1 = (color[i][j - 1][1] + color[i][j][1] + color[i][j + 1][1]);
			}
			else if (abs(avg0 - (color[row / 2][j - 1][0] + color[row / 2][j][0] + color[row / 2][j + 1][0])) > 100) {
				right2 = j;
				cout << "3   " << j << "\n";
				break;
			}

		}
		if (right3 < right2)
			right3 = right2;
	}

			   



	
	/*  연달아서 2개 3개 평균 비교해보기

	for (int i = row / 2; i < row - 1; i++) {
		if (color[i][col/2][0]>sum_row0+30&&
			color[i][col / 2][1] > sum_row1 + 30) {
			cout << i << ", ";
	//		a = i;
			break;
		}
	}

	for (int i = row / 2; i > 0; i--) {
		if (color[i][col / 2][0] > sum_row0 + 30 &&
			color[i][col / 2][1] > sum_row1 + 30) {
			cout << i << ", ";
	//		b = i;
			break;
		}
	}

	for (int j = col / 2; j < col - 1; j++) {
		if (color[row/2][j][0] > sum_col0 + 10 &&
			color[row / 2][j][1] > sum_col1 + 10) {
			cout << j << ", ";
			c = j;
			break;
		}
	}

	for (int j = col / 2; j > 0; j--) {
		if (color[row / 2][j][0] > sum_col0 + 10 &&
			color[row / 2][j][1] > sum_col1 + 10) {
			cout << j << ", ";
			d = j;
			break;
		}
	}
	*/

	/*
	
	for (int i = row / 2; i < row - 1; i++) {
		if ((abs(sum_row0 - color[i][col / 2][0]) +
			abs(sum_row1 - color[i][col / 2][1]) +
			abs(color[row / 2][col / 2][2] - color[i][col / 2][2])) > 150) {
			cout << i << ", ";
			a = i;
			break;
		}
	}

	for (int i = row / 2; i > 0; i--) {
		if ((abs(sum_row0 - color[i][col / 2][0]) +
			abs(sum_row1 - color[i][col / 2][1]) +
				abs(color[row / 2][col / 2][2] - color[i][col / 2][2])) > 150) {
			cout << i << ", ";
			b = i;
			break;
		}
	}
	for (int j = col / 2; j < col - 1; j++) {
		if ((abs(sum_col0 - color[row / 2][j][0]) +
			abs(sum_col1 - color[row / 2][j][1]) +
			abs(color[row / 2][col / 2][2] - color[i][col / 2][2])) > 150) {
			cout << j << ", ";
			c = j;
			break;
		}
	}
	for (int j = col / 2; j > 0; j--) {
		cout << abs(sum_col0 - color[row / 2][j][0]) + abs(sum_col1 - color[row / 2][j][1]);
		cout << "\n";
		if ((abs(sum_col0 - color[row / 2][j][0]) +
			abs(sum_col1 - color[row / 2][j][1]) +
			abs(color[row / 2][col / 2][2] - color[i][col / 2][2])) > 150) {
			cout << j << ", ";
			d = j;
			break;
		}
	}
	*/
/*	int sub=0;
	for (int i = row/2; i < row-10; i++) {
		if(sub < color[i + 10][col / 2][0] - color[i][col / 2][0]+color[i + 10][col / 2][1] - color[i][col / 2][1]){
			a = i;
			sub = color[i +10][col / 2][0] - color[i][col / 2][0] + color[i + 10][col / 2][1] - color[i][col / 2][1];
			cout << "a" <<sub << "\t"<< a << "\n";
		}
	}
	sub = 0;
	for (int i = row / 2; i > 10; i--) {
		if (sub < color[i + 10][col / 2][0] - color[i][col / 2][0] + color[i + 10][col / 2][1] - color[i][col / 2][1]) {
			b = i;
			sub = color[i + 10][col / 2][0] - color[i][col / 2][0] + color[i + 10][col / 2][1] - color[i][col / 2][1];
			cout << "b" << sub << "\t" << b << "\n";

		}
	}

	sub = 0;
	for (int j = col / 2; j < col-10; j++) {
		if (sub < color[row/2][j+10][0] - color[row/2][j][0] + color[row/2][j+10][1] - color[row/2][j][1]) {
			c = j;
			sub = color[row / 2][j + 10][0] - color[row / 2][j][0] + color[row / 2][j + 10][1] - color[row / 2][j][1];
			cout << "c" << sub << "\t" << c << "\n";

		}
	}

	sub = 0;
	for (int j = col / 2; j > 10; j--) {
		if (sub < color[row / 2][j + 10][0] - color[row / 2][j][0] + color[row / 2][j + 10][1] - color[row / 2][j][1]) {
			d = j;
			sub = color[row / 2][j + 10][0] - color[row / 2][j][0] + color[row / 2][j + 10][1] - color[row / 2][j][1];
			cout << "d" << sub << "\t" << d << "\n";

		}
	}*/
	//cout << a <<"\t"<< b << "\t" << c << "\t" << d;


	for (int j = 0; j < col; j++) {
		image.at<cv::Vec3b>(up3, j)[2] = 255;
		image.at<cv::Vec3b>(up3, j)[1] = 255;
		image.at<cv::Vec3b>(up3, j)[0] = 255;
	}
	for (int j = 0; j < col; j++) {
		image.at<cv::Vec3b>(down3, j)[2] = 255;
		image.at<cv::Vec3b>(down3, j)[1] = 255;
		image.at<cv::Vec3b>(down3, j)[0] = 255;
	}
	for (int i = 0; i < row; i++) {
		image.at<cv::Vec3b>(i, left3)[2] = 255;
		image.at<cv::Vec3b>(i, left3)[1] = 255;
		image.at<cv::Vec3b>(i, left3)[0] = 255;
	}
	for (int i = 0; i < row; i++) {
		image.at<cv::Vec3b>(i, right3)[2] = 255;
		image.at<cv::Vec3b>(i, right3)[1] = 255;
		image.at<cv::Vec3b>(i, right3)[0] = 255;
	}
	


	// create 4 windows
	cv::namedWindow("Original Image");


	// show 4 windows
	cv::imshow("Original Image", image);
	cv::waitKey(0);


	return 0;
}

