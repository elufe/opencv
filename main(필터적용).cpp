
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
			}// 밑에 수정...
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

		markerImage.convertTo(markers, CV_32S); //32비트마커스로자료형변환

	}

	cv::Mat process(const cv::Mat& image) {

		cv::watershed(image, markers);

		//분할결과를markers에저장

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
	cv::Mat image = cv::imread("C:/Users/msi/Desktop/aaa.jpg", cv::IMREAD_COLOR);//원본 이미지
	int row = image.rows;//470 세로 427
	int col = image.cols;//624 가로 398
	cv::Mat black = masking(image, row, col);//흑백 이미지
	cv::Mat capture = cutting(image, black, row, col);//잘린 이미지
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
		cv::cvtColor(image, gray_image, CV_BGR2GRAY); // 흑백영상으로 변환

		cv::namedWindow("Gray_image");
		cv::imshow("Gray_image", gray_image);  // 흑백 영상 출력

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
		cv::cvtColor(image, gray_image, CV_BGR2GRAY); // 흑백영상으로 변환

		cv::namedWindow("Gray_image");
		cv::imshow("Gray_image", gray_image);  // 흑백 영상 출력

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

	cv::imshow("Original Image", image2); //원본

	cv::Mat gray_image;

	cv::cvtColor(image2, gray_image, CV_BGR2GRAY);

	cv::imshow("Gray Image", gray_image); //gray영상

	cv::Mat binary_image;

	cv::threshold(gray_image, binary_image, 90, 255, cv::THRESH_BINARY_INV);

	cv::imshow("Binary Image", binary_image); //이진영상으로변환(손하얗게끔inverse)


	cv::Mat fg;

	cv::erode(binary_image, fg, cv::Mat(), cv::Point(-1, -1), 15); //침식

	cv::imshow("Foreground", fg);


	cv::Mat bg;

	cv::dilate(binary_image, bg, cv::Mat(), cv::Point(-1, -1), 40); //팽창

	cv::threshold(bg, bg, 1, 128, cv::THRESH_BINARY_INV);

	//(1보다작은)배경을128, (1보다큰)객체0. Threshold설정INVERSE 적용.

	cv::imshow("Background", bg);


	cv::Mat markers(binary_image.size(), CV_8U, cv::Scalar(0));

	markers = fg + bg; //침식+팽창= 마커영상으로조합. 워터쉐드알고리즘에 입력으로 사용됨.

	cv::imshow("Marker", markers);


	WatershedSegmenter segmenter; //워터쉐드분할객체생성

	segmenter.setMarkers(markers); //set마커하면signed 이미지로바뀜

	segmenter.process(image2); //0,128,255로구성됨

	cv::imshow("Segmentation", segmenter.getSegmentation());


	cv::imshow("Watershed", segmenter.getWatersheds()); // 0,255로구성됨






	histogram(capture);//색조 판단
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

	for (int i = 0; i < 5; i++) { //중간점 주변 25 픽셀의 rgb값의 평균 계산
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
	cv::inRange(image, cv::Scalar((blue*0.3), (green*0.3), (red*0.3)), cv::Scalar((blue*1.3), (green*1.3), (red*1.3)), black);//평균 rgb의 상한값과 하한값 사이 마스킹
	cv::Mat mask = cv::getStructuringElement(cv::MORPH_RECT, cv::Size(3, 3), cv::Point(1, 1));//감산 연산용 마스킹
	cv::erode(black, black, /*cv::Mat(3, 3, CV_8U, cv::Scalar(1))*/mask, cv::Point(-1, -1), 1);//감산연산 진행(노이즈 캔슬링)

	return black;//흑백으로 마스킹된 이미지 반환
}

cv::Mat cutting(cv::Mat image, cv::Mat black, const int row, const int col) {//마스킹된 이미지를 기반으로 원본 이미지를 자름
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
	if (!(left == 0 || right == 0 || top == 0 || bottom == 0))//예외 처리
		capture = image(cv::Range(top, bottom), cv::Range(left, right));

	return capture;//잘린 이미지 리턴
}

void histogram(cv::Mat capture) {
	cv::Mat dst;
	cv::Mat bgr[3];
	cv::Mat hist; //Histogram 계산값 저장
	int channel[] = { 0,1,2 };
	int histSize = 255; //Histogram 가로값의 수
	int count = 0;
	float range[] = { 0,255.0 };
	const float * ranges = range;
	int hist_w = 512; int hist_h = 400;
	int number_bins = 255;
	int bin_w = cvRound((double)hist_w / number_bins);
	unsigned row2 = capture.rows; unsigned col2 = capture.cols; //자른 사진의 크기 저장

	cvtColor(capture, dst, CV_HSV2BGR); //Color 변경
	calcHist(&dst, 3, channel, cv::Mat(), hist, 1, &histSize, &ranges, true, false); //Histogram 계산
	cv::Mat histImage(hist_h, hist_w, CV_8UC3, cv::Scalar(0, 0, 0));
	normalize(hist, hist, 0, histImage.rows, cv::NORM_MINMAX, -1, cv::Mat());

	for (int i = 1; i < number_bins; i++) {	//Histogram 선 그리기
		line(histImage, cv::Point(bin_w*(i - 1), hist_h - cvRound(hist.at<float>(i - 1))), cv::Point(bin_w*(i), hist_h - cvRound(hist.at<float>(i))), cv::Scalar(0, 255, 0), 2, 8, 0);
	}

	for (int i = 0; i < histSize; i++) { //색의 다양성 검출
		printf("%d번째 %f \n", i, hist.at<float>(i));
		if (hist.at<float>(i) > 229) {
			count++;
		}
	}

	printf("카운트 수 : %d\n", count);

	if (count > 15) {
		printf("다양한 색조를 보입니다.");
	}
	else {
		printf("다양한 색조를 보이지 않습니다.");
	}

	cv::namedWindow("Histogram", CV_WINDOW_AUTOSIZE);
	cv::imshow("HSV2BGR", dst);
	cv::imshow("Histogram", histImage);
}


