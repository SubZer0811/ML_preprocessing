import cv2
import os
import argparse

def main (args):

	cap = cv2.VideoCapture(args.vid_path)
	vid_id = args.vid_path.split('/')[-1].split('.')[0]

	count = 1
	ret, frame = cap.read()

	while(ret):

		file_name = f"{vid_id}_{count}.jpg"
		file_path = f"{args.out_path}/{file_name}"
		print(file_path)

		cv2.imwrite(file_path, frame)

		while count % args.n != 0:
			count += 1
			ret, frame = cap.read()

		count += 1

if __name__ == "__main__":
	argpar = argparse.ArgumentParser()
	
	argpar.add_argument("vid_path", type=str, help="Path to input video")
	argpar.add_argument("out_path", type=str, help="Path to output directory")
	argpar.add_argument("--n", type=int, default=10, help="1 frame to save in 'n' frames")

	args = argpar.parse_args()

	if(not os.path.exists(args.vid_path)):
		print(f"[!] {args.vid_path}: File does not exist")
		exit(0)
	if(not os.path.exists(args.out_path)):
		print(f"[!] {args.out_path}: Folder does not exist")
		exit(0)

	main(args)