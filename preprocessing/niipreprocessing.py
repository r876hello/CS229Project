import scipy, numpy, shutil, os, nibabel
import sys, getopt
from pathlib import Path
import imageio


def main(input, output):
    inputfile = input
    outputfile = output
    """
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('nii2png.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('nii2png.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
    """

    print('Input file is ', inputfile)
    print('Output folder is ', outputfile)

    # set fn as your 4d nifti file
    image_array = nibabel.load(inputfile).get_data()
    print(len(image_array.shape))


    # if 4D image inputted
    if len(image_array.shape) == 4:
        print("ERROR", inputfile)
        exit()

    # else if 3D image inputted
    elif len(image_array.shape) == 3:
        # set 4d array dimension values

        nx, ny, nz = image_array.shape

        # set destination folder
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)
            print("Created ouput directory: ", outputfile)

        print('Reading NIfTI file...')

        total_slices = image_array.shape[2]

        slice_counter = 0
        # iterate through slices
        for current_slice in range(20, total_slices - 20):
            # alternate slices
            if (slice_counter % 1) == 0:
                # rotate or no rotate

                data = image_array[:, :, current_slice]

                #alternate slices and save as png
                if (slice_counter % 1) == 0:
                    print('Saving image...')
                    fileName = list(outputfile.parts)[-1]
                    image_name = fileName + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    imageio.imwrite(image_name, data)
                    print('Saved.')

                    #move images to folder
                    print('Moving image...')
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1
                    print('Moved.')

        print('Finished converting images')
    else:
        print('Not a 3D or 4D Image. Please try again.')

# call the function to start the program
if __name__ == "__main__":
    files = list(Path(".").rglob("*.nii"))
    for i in files:
        print(i)
        new = list(i.parts)
        new[-1] = new[-1][0:-4]
        output = Path(*new)
        main(i, output)
    
