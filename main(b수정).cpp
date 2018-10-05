#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace std;

cv::Mat masking(cv::Mat);//return masking image
cv::Mat masking2(cv::Mat);
void fill(cv::Mat);
int * find(cv::Mat);//return left,right,top,bottom
cv::Mat cutting(cv::Mat, int *);//return cuting image
void histogram(cv::Mat);
float symmetry(cv::Mat);// return degree of symmetry
void boundary(int * index1, int * index2);


int main(int argc, char* argv[]) {
	string name = "case3.jpg";
	cv::Mat image = cv::imread("C:/Users/msi/Desktop/" + name, cv::IMREAD_COLOR);//���� �̹���
	cv::Mat original = cv::imread("C:/Users/msi/Desktop/" + name, cv::IMREAD_COLOR);//���� �̹���
	cv::Mat bcompare1 = cv::imread("C:/Users/msi/Desktop/" + name, cv::IMREAD_COLOR);//���� �̹���
	cv::Mat bcompare2 = cv::imread("C:/Users/msi/Desktop/" + name, cv::IMREAD_COLOR);//���� �̹���
	cv::imshow("img", image);
	int row = image.rows;//����
	int col = image.cols;//����
	cv::Mat black = masking(image);
	cv::Mat b1 = masking2(bcompare1);
//	cv::Mat b2 = masking(bcompare2);
	cv::imshow("black", black);
	int * index = find(black);
	int * index2 = find(b1);
	boundary(index,index2);

	cv::Mat capture = cutting(black, index);
	original = cutting(original, index);
	bcompare2 = cutting(bcompare2, index2);
	fill(capture);

//	cout << "symmetry : " << symmetry(original) << endl;
	cv::imshow("origi", original);
	cv::imshow("origi2", bcompare2);
	histogram(original);
	cv::waitKey(0);
	return 0;
}

void boundary(int * index1, int * index2) {
	int size1, size2;
	size1 = (index1[1] - index1[0])*(index1[3] - index1[2]);
	size2 = (index2[1] - index2[0])*(index2[3] - index2[2]);
	cout << "left" << index1[0]<<"right" << index1[1] << "top" << index1[2] << "bottom" << index1[3] <<"\n";
	cout << "left" << index2[0] << "right" << index2[1] << "top" << index2[2] << "bottom" << index2[3] << "\n";

	cout << "������� ���� : " << (float)size2 / size1 * 100<<"\n";
	if (((float)size2 / size1 * 100) > 100 && ((float)size2 / size1 * 100) < 200)
		cout << "��輱�� ��ȣ�մϴ�"<<"\n";

}

cv::Mat masking(cv::Mat image) {
	cv::Mat black;
	cv::Mat gray_image;
	medianBlur(image, image, 7);
	cv::cvtColor(image, gray_image, CV_BGR2GRAY); // ��鿵������ ��ȯ
	cv::adaptiveThreshold(gray_image, black, 255, cv::ADAPTIVE_THRESH_MEAN_C, cv::THRESH_BINARY, 401, 60);
	return black;//������� ����ŷ�� �̹��� ��ȯ
}

cv::Mat masking2(cv::Mat image) {
	cv::Mat black;
	cv::Mat gray_image;
	medianBlur(image, image, 7);
	cv::cvtColor(image, gray_image, CV_BGR2GRAY); // ��鿵������ ��ȯ
	cv::adaptiveThreshold(gray_image, black, 255, cv::ADAPTIVE_THRESH_MEAN_C, cv::THRESH_BINARY, 401, 50);
	return black;//������� ����ŷ�� �̹��� ��ȯ
}


void fill(cv::Mat black) {
	int row = black.rows;
	int col = black.cols;
	int read = -1;
	int start = 0;
	int end = 0;

	for (int i = 0; i < row; i++) {
		int x = col - 1;
		while (x >= 0) {
			read = black.at<uchar>(i, x);
			if (read == 0) {
				end = x;
				break;
			}
			x--;
		}
		x = 0;
		while (x < col) {
			read = black.at<uchar>(i, x);
			if (read == 0) {
				start = x;
				break;
			}
			x++;
		}
		for (int j = start; j < end; j++)
			black.at<uchar>(i, j) = 0;
		start = 0;
		end = 0;
	}

	for (int i = 0; i < col; i++) {
		int x = row - 1;
		while (x >= 0) {
			read = black.at<uchar>(x, i);
			if (read == 0) {
				end = x;
				break;
			}
			x--;
		}
		x = 0;
		while (x < row) {
			read = black.at<uchar>(x, i);
			if (read == 0) {
				start = x;
				break;
			}
			x++;
		}
		for (int j = start; j < end; j++)
			black.at<uchar>(j, i) = 0;
		start = 0;
		end = 0;
	}
}

int * find(cv::Mat black) {
	int row = black.rows;
	int col = black.cols;
	int left = 0, right = 0, top = 0, bottom = 0;
	int read = -1;
	bool flag = false;
	for (int i = 0; i < row; i++) {//find top
		for (int j = 0; j < col; j++) {
			read = black.at<uchar>(i, j);
			if (read == 0) {
				top = i;
				read = -1;
				flag = true;
				break;
			}
		}
		if (flag) {
			flag = false;
			break;
		}
	}
	for (int i = row - 1; i >= 0; i--) {//find bottom
		for (int j = 0; j < col; j++) {
			read = black.at<uchar>(i, j);
			if (read == 0) {
				bottom = i;
				read = -1;
				flag = true;
				break;
			}
		}
		if (flag) {
			flag = false;
			break;
		}
	}
	for (int i = 0; i < col; i++) {//find left
		for (int j = 0; j < row; j++) {
			read = black.at<uchar>(j, i);
			if (read == 0) {
				left = i;
				read = -1;
				flag = true;
				break;
			}
		}
		if (flag) {
			flag = false;
			break;
		}
	}
	for (int i = col - 1; i >= 0; i--) {//find right
		for (int j = 0; j < row; j++) {
			read = black.at<uchar>(j, i);
			if (read == 0) {
				right = i;
				read = -1;
				flag = true;
				break;
			}
		}
		if (flag) {
			flag = false;
			break;
		}
	}
	cout << "left" << left << "right" << right << endl;
	cout << "top" << top << "bottom" << bottom << endl;
	int * index = (int *)malloc(sizeof(int) * 4);
	index[0] = left;
	index[1] = right;
	index[2] = top;
	index[3] = bottom;
	return index;
}//884281
cv::Mat cutting(cv::Mat image, int * index) {//����ŷ�� �̹����� ������� ���� �̹����� �ڸ�
	int left = index[0];
	int right = index[1];
	int top = index[2];
	int bottom = index[3];

	cv::Mat capture = image;
	if (!(left == 0 || right == 0 || top == 0 || bottom == 0))//���� ó��
		capture = image(cv::Range(top, bottom), cv::Range(left, right));

	return capture;//�߸� �̹��� ����
}

float symmetry(cv::Mat image) {
	int row = image.rows;
	int col = image.cols;
	int end_top = 0, start_bottom = row / 2;

	if (row % 2 == 0) // even
		end_top = row / 2;
	else //odd
		end_top = (row / 2) + 1; // row�� ¦���� Ȧ���� �յ��ϰ� ����

	cv::Mat top = image(cv::Range(0, end_top), cv::Range(0, col));
	cv::Mat bottom = image(cv::Range(start_bottom, row), cv::Range(0, col));
	cv::flip(bottom, bottom, -1);
	int count = 0;
	int read_top = -1, read_bottom = -1;
	for (int i = 0; i < end_top; i++) {
		for (int j = 0; j < col; j++) {
			read_top = top.at<uchar>(i, j);
			read_bottom = bottom.at<uchar>(i, j);
			if (read_top != read_bottom) {
				count++;
			}
		}
	}
	cv::imshow("top", top);
	cv::imshow("bottom", bottom);
	float matrix = end_top * col;
	return (float)((matrix - count) / matrix);
}

void histogram(cv::Mat capture) { // 30����
	cv::Mat dst;
	cv::Mat bgr[3];
	cv::Mat hist; //Histogram ��갪 ����
	int channel[] = { 0,1,2 };
	int histSize = 255; //Histogram ���ΰ��� ��
	int count = 0;
	float range[] = { 0,255.0 };
	const float * ranges = range;
	int hist_w = 512; int hist_h = 400;
	int number_bins = 255;
	int bin_w = cvRound((double)hist_w / number_bins);
	unsigned row2 = capture.rows; unsigned col2 = capture.cols; //�ڸ� ������ ũ�� ����

	cvtColor(capture, dst, CV_HSV2BGR); //Color ����
	calcHist(&dst, 3, channel, cv::Mat(), hist, 1, &histSize, &ranges, true, false); //Histogram ���
	cv::Mat histImage(hist_h, hist_w, CV_8UC3, cv::Scalar(0, 0, 0));
	normalize(hist, hist, 0, histImage.rows, cv::NORM_MINMAX, -1, cv::Mat());

	for (int i = 1; i < number_bins; i++) {	//Histogram �� �׸���
		line(histImage, cv::Point(bin_w*(i - 1), hist_h - cvRound(hist.at<float>(i - 1))), cv::Point(bin_w*(i), hist_h - cvRound(hist.at<float>(i))), cv::Scalar(0, 255, 0), 2, 8, 0);
	}

	for (int i = 0; i < histSize; i++) { //���� �پ缺 ����
		//printf("%d��° %f \n", i, hist.at<float>(i));
		if (hist.at<float>(i) > 229) {
			count++;
		}
	}

	printf("ī��Ʈ �� : %d\n", count);

	if (count > 10) {
		printf("�پ��� ������ ���Դϴ�.");
	}
	else {
		printf("�پ��� ������ ������ �ʽ��ϴ�.");
	}

	cv::namedWindow("Histogram", CV_WINDOW_AUTOSIZE);
	cv::imshow("HSV2BGR", dst);
	cv::imshow("Histogram", histImage);
}