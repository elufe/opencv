
#include <iostream>
#include <cstdio>
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
using namespace std;

#include <opencv2\core\core.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>

#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>



cv::Mat masking(cv::Mat, int, int);//return masking image
cv::Mat cutting(cv::Mat, cv::Mat, int, int);//return cuting image
void histogram(cv::Mat);


void fucking(cv::Mat image) {

	int b = 0, g = 0, r = 0;

	for (int i = 3; i < image.rows/2; i += 1) {
		for (int j = 3; j < image.cols/2; j += 1) {

			/*for (int a = i; a < i + 5; a++) {
				for (int b = j; b < j + 5; b++) {
					b += image.at<cv::Vec3b>(a, b)[0];
					g += image.at<cv::Vec3b>(a, b)[1];
					r += image.at<cv::Vec3b>(a, b)[2];
				}
			}// �ؿ� ����...
			for (int a = i; a < i + 5; a++) {
				for (int b = j; b < j + 5; b++) {
				//	if (image.at<cv::Vec3b>(a, b)[0] < 30 && image.at<cv::Vec3b>(a, b)[1] < 30 && image.at<cv::Vec3b>(a, b)[2] < 30) {

				//		cout << "1";
				//	}
				/*
					if (image.at<cv::Vec3b>(a, b)[1] - g / 9 < 0) {
						cout << "2";
						image.at<cv::Vec3b>(a, b)[1] = g / 9;
					}
					if (image.at<cv::Vec3b>(a, b)[2] - r / 9 < 0) {
						image.at<cv::Vec3b>(a, b)[2] = r / 9;

						cout << "3";
					}

				}
			}

			b = 0;
			g = 0;
			r = 0;*/
		}
	}

	cv::imshow("original222", image);

	cv::waitKey(0);
}


class WatershedSegmenter {

private:

	cv::Mat markers;

public:

	void setMarkers(const cv::Mat& markerImage) {

		markerImage.convertTo(markers, CV_32S); //32��Ʈ��Ŀ�����ڷ�����ȯ

	}

	cv::Mat process(const cv::Mat& image) {

		cv::watershed(image, markers);

		//���Ұ����markers������

		return markers;

	}

	cv::Mat getSegmentation() {

		cv::Mat tmp;

		markers.convertTo(tmp, CV_8U); return tmp;

	}

	cv::Mat getWatersheds() {

		cv::Mat tmp;

		markers.convertTo(tmp, CV_8U, 255, 255); return tmp;

	}

};




int main(int argc, char* argv[]) {
	cv::Mat image = cv::imread("C:/Users/msi/Desktop/aaa.jpg", cv::IMREAD_COLOR);//���� �̹���
	int row = image.rows;//470 ���� 427
	int col = image.cols;//624 ���� 398
	cv::Mat black = masking(image, row, col);//��� �̹���
	cv::Mat capture = cutting(image, black, row, col);//�߸� �̹���
	cv::Mat imageb;
	cv::Mat imageg;
	cv::Mat imagem;
	cv::Mat imagebi;
	

//	fucking(image);

//	medianBlur(image, image, 5);

//	blur(image, imageb, Size(5, 5));
//	cv::imshow("blur result", imageb);

//	GaussianBlur(image, imageg, Size(5, 5), 1.5, 1.5);
//	cv::imshow("GaussianBlur result", imageg);


//	bilateralFilter(image, imagebi, 10, 50, 50);
//	cv::imshow("bilateralFilter result", imagebi);




	while (true)
	{
		cv::namedWindow("image_001");
		cv::imshow("image_001", image);

		cv::Mat gray_image;
		cv::cvtColor(image, gray_image, CV_BGR2GRAY); // ��鿵������ ��ȯ

		cv::namedWindow("Gray_image");
		cv::imshow("Gray_image", gray_image);  // ��� ���� ���

		// get a adaptive threshold image
		cv::Mat athimage;
		cv::adaptiveThreshold(gray_image, athimage, 255,
			cv::ADAPTIVE_THRESH_MEAN_C,
			cv::THRESH_BINARY, 401, 60);
		cv::Mat athimage2;
		cv::adaptiveThreshold(gray_image, athimage2, 255,
			cv::ADAPTIVE_THRESH_MEAN_C,
			cv::THRESH_BINARY, 401, 50);


		cv::namedWindow("Threshold Image");
		cv::imshow("Threshold Image", athimage);

		cv::namedWindow("Threshold Image2");
		cv::imshow("Threshold Image2", athimage2);

		int key = cv::waitKey(10);

		if (key == 27)      //ESC key
			break;
	}


	medianBlur(image, image, 7);
	cv::imshow("medianBlur result", image);
	while (true)
	{
		cv::namedWindow("image_001");
		cv::imshow("image_001", image);

		cv::Mat gray_image;
		cv::cvtColor(image, gray_image, CV_BGR2GRAY); // ��鿵������ ��ȯ

		cv::namedWindow("Gray_image");
		cv::imshow("Gray_image", gray_image);  // ��� ���� ���

		// get a adaptive threshold image
		cv::Mat athimage;
		cv::adaptiveThreshold(gray_image, athimage, 255,
			cv::ADAPTIVE_THRESH_MEAN_C,
			cv::THRESH_BINARY, 401, 60);
		cv::Mat athimage2;
		cv::adaptiveThreshold(gray_image, athimage2, 255,
			cv::ADAPTIVE_THRESH_MEAN_C,
			cv::THRESH_BINARY, 401, 50);


		cv::namedWindow("Threshold Image33");
		cv::imshow("Threshold Image33", athimage);

		cv::namedWindow("Threshold Image233");
		cv::imshow("Threshold Image233", athimage2);

		int key = cv::waitKey(10);

		if (key == 27)      //ESC key
			break;
	}




	cv::Mat image2 = image;

	cv::imshow("Original Image", image2); //����

	cv::Mat gray_image;

	cv::cvtColor(image2, gray_image, CV_BGR2GRAY);

	cv::imshow("Gray Image", gray_image); //gray����

	cv::Mat binary_image;

	cv::threshold(gray_image, binary_image, 90, 255, cv::THRESH_BINARY_INV);

	cv::imshow("Binary Image", binary_image); //�����������κ�ȯ(���Ͼ�Բ�inverse)


	cv::Mat fg;

	cv::erode(binary_image, fg, cv::Mat(), cv::Point(-1, -1), 15); //ħ��

	cv::imshow("Foreground", fg);


	cv::Mat bg;

	cv::dilate(binary_image, bg, cv::Mat(), cv::Point(-1, -1), 40); //��â

	cv::threshold(bg, bg, 1, 128, cv::THRESH_BINARY_INV);

	//(1��������)�����128, (1����ū)��ü0. Threshold����INVERSE ����.

	cv::imshow("Background", bg);


	cv::Mat markers(binary_image.size(), CV_8U, cv::Scalar(0));

	markers = fg + bg; //ħ��+��â= ��Ŀ������������. ���ͽ���˰��� �Է����� ����.

	cv::imshow("Marker", markers);


	WatershedSegmenter segmenter; //���ͽ�����Ұ�ü����

	segmenter.setMarkers(markers); //set��Ŀ�ϸ�signed �̹����ιٲ�

	segmenter.process(image2); //0,128,255�α�����

	cv::imshow("Segmentation", segmenter.getSegmentation());


	cv::imshow("Watershed", segmenter.getWatersheds()); // 0,255�α�����






	histogram(capture);//���� �Ǵ�
	cv::imshow("original", image);
	cv::imshow("masking", black);
	cv::imshow("slice", capture);

	cv::waitKey(0);
	return 0;

}

cv::Mat masking(cv::Mat image, const int row, const int col) {
	int row_start = (row / 2) - 2;
	int col_start = (col / 2) - 2;
	int red = 0, green = 0, blue = 0;

	for (int i = 0; i < 5; i++) { //�߰��� �ֺ� 25 �ȼ��� rgb���� ��� ���
		for (int j = 0; j < 5; j++) {
			red += image.at<cv::Vec3b>(i + row_start, j + col_start)[2];
			green += image.at<cv::Vec3b>(i + row_start, j + col_start)[1];
			blue += image.at<cv::Vec3b>(i + row_start, j + col_start)[0];
		}
	}
	red /= 25;
	green /= 25;
	blue /= 25;

	cout << "rgb : " << red * 0.3 << ", " << green * 0.3 << ", " << blue * 0.3 << endl;
	cout << "rgb : " << red * 1.3 << ", " << green * 1.3 << ", " << blue * 1.3 << endl;

	cv::Mat black;
	cv::inRange(image, cv::Scalar((blue*0.3), (green*0.3), (red*0.3)), cv::Scalar((blue*1.3), (green*1.3), (red*1.3)), black);//��� rgb�� ���Ѱ��� ���Ѱ� ���� ����ŷ
	cv::Mat mask = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3), cv::Point(1, 1));//���� ����� ����ŷ
	cv::erode(black, black, /*cv::Mat(3, 3, CV_8U, cv::Scalar(1))*/mask, cv::Point(-1, -1), 1);//���꿬�� ����(������ ĵ����)

	return black;//������� ����ŷ�� �̹��� ��ȯ
}

cv::Mat cutting(cv::Mat image, cv::Mat black, const int row, const int col) {//����ŷ�� �̹����� ������� ���� �̹����� �ڸ�
	int left = 0, right = 0, top = 0, bottom = 0;
	int read = -1;
	bool flag = false;
	for (int i = 0; i < row; i++) {//find top
		for (int j = 0; j < col; j++) {
			read = black.at<uchar>(i, j);
			if (read == 255) {
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
			if (read == 255) {
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
			if (read == 255) {
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
			if (read == 255) {
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

	cv::Mat capture = image;
	if (!(left == 0 || right == 0 || top == 0 || bottom == 0))//���� ó��
		capture = image(cv::Range(top, bottom), cv::Range(left, right));

	return capture;//�߸� �̹��� ����
}

void histogram(cv::Mat capture) {
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
		printf("%d��° %f \n", i, hist.at<float>(i));
		if (hist.at<float>(i) > 229) {
			count++;
		}
	}

	printf("ī��Ʈ �� : %d\n", count);

	if (count > 15) {
		printf("�پ��� ������ ���Դϴ�.");
	}
	else {
		printf("�پ��� ������ ������ �ʽ��ϴ�.");
	}

	cv::namedWindow("Histogram", CV_WINDOW_AUTOSIZE);
	cv::imshow("HSV2BGR", dst);
	cv::imshow("Histogram", histImage);
}


