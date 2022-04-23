import os
import logging
from astropy.io import fits

from csst_dfs_commons.logging import setup_logging
from csst_dfs_api.ifs import Level0DataApi, CalMergeApi, Level1DataApi
setup_logging()

log = logging.getLogger('csst')

class RSS(object):

    def __init__(self, file_name):
        self.root_dir = os.getenv("CSST_LOCAL_FILE_ROOT", "/opt/temp/csst")
        self.level0Api = Level0DataApi()
        self.calibrationApi = CalMergeApi()
        self.level1Api = Level1DataApi()
        
        try:
            self.raw = self.level0Api.find(file_name=file_name)
            self.raw = self.raw.data[0] if self.raw.success else None

            if self.raw is None:
                log.error('raw %s not found' %(file_name,))
            else:
                log.info("find raw fits: %s,%s"%(self.raw["id"], self.raw["filename"]))

        except Exception as e:
            log.error('raw %s not found' %(file_name,),e)

    def set_bias(self, file_name=None):
        try:
            self.bias = self.calibrationApi.find(file_name=file_name, ref_type="bias")
            self.bias = self.bias.data[0] if self.bias.success else None
            
            if self.bias is None:
                log.error('bias %s not found' %(file_name,))
            else:
                log.info("find ref bias fits: %s,%s"%(self.bias["id"], self.bias["filename"]))
        except Exception as e:
            log.error('bias %s not found' %(file_name,),e)

    def set_flat(self, file_name=None):
        try:
            self.flat = self.calibrationApi.find(file_name=file_name, ref_type="flat")
            self.flat = self.flat.data[0] if self.flat.success else None
            
            if self.flat is None:
                log.error('flat %s not found' %(file_name,))
            else:
                log.info("find ref flat fits: %s,%s"%(self.flat["id"], self.flat["filename"]))
        except Exception as e:
            log.error('flat %s not found' %(file_name,),e)

    def set_arc(self, file_name = None):
        try:
            self.arc = self.calibrationApi.find(file_name=file_name, ref_type="arc")
            self.arc = self.arc.data[0] if self.arc.success else None

            if self.arc is None:
                log.error('arc %s not found' %(file_name,))
            else:
                log.info("find ref arc fits: %s,%s"%(self.arc["id"], self.arc["filename"]))
        except Exception as e:
            log.error('arc %s not found' %(file_name,),e)

    def set_sky(self, file_name = None):
        try:
            self.sky = self.calibrationApi.find(file_name=file_name, ref_type="sky")
            self.sky = self.sky.data[0] if self.sky.success else None

            if self.sky is None:
                log.error('sky %s not found' %(file_name,))
            else:
                log.info("find ref sky fits: %s,%s"%(self.sky["id"], self.sky["filename"]))
        except Exception as e:
            log.error('sky %s not found' %(file_name,),e)

    def makecube(self, outfile):
        if self.raw is None:
            log.error('raw not found')
            return
        if self.arc is None:
            log.error('arc not found')
            return
        if self.flat is None:
            log.error('flat not found')
            return
        if self.sky is None:
            log.error('sky not found')
            return

        hdul_raw = fits.open(os.path.join(self.raw.file_path))
        hdul_arc = fits.open(os.path.join(self.arc.file_path))
        hdul_flat = fits.open(os.path.join(self.flat.file_path))
        hdul_sky  = fits.open(os.path.join(self.sky.file_path))

        hdul_raw.append(hdul_arc[0])
        hdul_raw.append(hdul_flat[0])
        hdul_raw.append(hdul_sky[0])

        hdul_raw.writeto(outfile, overwrite=True)

        self.level1Api.write(level0_id = self.raw.id, 
            data_type = "sci",
            cor_sci_id = 2,
            prc_params = "/opt/dddasd.params",
            flat_id = self.flat.id,
            dark_id = -1,
            bias_id = -1,
            lamp_id = -1,
            arc_id = self.arc.id,
            sky_id = self.sky.id,            
            prc_status = 0,
            filename = "rss_demo1",
            file_path = outfile,
            pipeline_id = "P2")

if __name__ == '__main__':
    rss1 = RSS('CCD1_ObsTime_300_ObsNum_1.fits')               # raw data
    # rss1.set_bias()                                             # currently no Bias file
    rss1.set_flat(file_name = 'Flat_flux.fits')                 # flat file
    rss1.set_arc(file_name = 'HgAr_flux.fits')                  # arc file
    rss1.set_sky(file_name = 'sky_noise_With_wavelength.fits')  # sky file

    rss1.makecube('/opt/temp/csst_ifs/rss_demo1.fits')
