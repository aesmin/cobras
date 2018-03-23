class Clustering:

    def __init__(self,clusters):
        self.clusters = clusters

    def get_super_instances(self):
        return [si for c in self.clusters for si in c.super_instances]

    def construct_cluster_labeling(self):

        pts_per_cluster = [cluster.get_all_points() for cluster in self.clusters]

        pred = [-1] * sum([len(x) for x in pts_per_cluster])

        for i, pts in enumerate(pts_per_cluster):
            for pt in pts:
                pred[pt] = i

        return pred


